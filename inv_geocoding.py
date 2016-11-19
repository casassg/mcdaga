import requests
import json
from skyscanner.skyscanner import Flights

def test_retry_on_http_errors(self):
        self.build_data.exc_to_raise = requests.HTTPError('err')

        # 2 http errors won't generate errors
        self.build_data.raises_for_indexes[10] = 2
        self.build_data.mid_point()

        # if 3 http errors are generated, it will be raised
        new_data = self.build_data[:10]
        new_data.raises_for_indexes[5] = 3
        self.assertRaises(errors.DownloadError, new_data.mid_point)

flights_service = Flights('el966379157751618466416148364616')
result = flights_service.get_result(
    country='UK',
    currency='GBP',
    locale='en-GB',
    originplace='SIN-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-05-28',
    inbounddate='2017-05-31',
    adults=1).parsed





def getAddressFromLatLng(latitude, longitude):
    
    # Did the geocoding request comes from a device with a
    # location sensor? Must be either true or false.
    sensor = 'false'

    # Hit Google's reverse geocoder directly
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
    #print url
    response = requests.get(url)
    #print response.json()['results'][0]['formatted_address']

getAddressFromLatLng(41.3714375,2.1352049)