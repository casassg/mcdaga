#!/usr/bin/python
import tweepy
import pprint
import urllib
import cv2
import json
import SimpleHTTPServer
import SocketServer
import string

ckey = "mg5dCqbGffBemIi0mGWLNQNu7"
csecret = "bnsxIA02tTycdPS8LVkJSojdcVzu7wOPbE4crI53URZ27cUKWj"
atoken = "930433105-MDrr9AImeXth1nWDjgFRK0i2ph9DMkn2ZLfQzD1l"
asecret = "Yr5g1Zp0ff7mMowW5sRvxJlKYoiFCblDjWYyDeYgpAoso"

OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret, 'access_token_key': atoken,
              'access_token_secret': asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)


class TweetInfo():
    def __init__(self):
        tweetID = ''


def showImage(filename):
    image = cv2.imread(filename)
    cv2.imshow('IMAGE', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def index():
    return render_template('live.html')


def search_tag(tag_name):
    cricTweet = tweepy.Cursor(api.search, q=tag_name, result_type='mixed').items(10)  # nombre de tweets a treure

    arrayTweets = []

    for tweet in cricTweet:
        print tweet.created_at, tweet.text, tweet.retweet_count, tweet.favorite_count
        twet = {'id': tweet.id}
        t = str(tweet.created_at)
        time = t.split(' ')
        twet['time'] = "Date: " + time[0] + " Time: " + time[1]
        print twet['time']
        twet['text'] = tweet.text
        twet['rt'] = tweet.retweet_count
        twet['fav'] = tweet.favorite_count
        twet['imurl'] = 'null'
        if 'media' in tweet.entities:
            media = tweet.entities['media'][0]
            im_url = media['media_url']
            filename = str(media['id']) + '.jpg'
            twet['imurl'] = im_url
            urllib.urlretrieve(im_url, "./tweet_photos/" + filename)

        arrayTweets.append(twet)

    json_data = json.dumps(arrayTweets)
    f = open("data.json", "w")
    f.write(json_data)
    f.close()
    print(json_data)


search_tag("mcdaga")

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
