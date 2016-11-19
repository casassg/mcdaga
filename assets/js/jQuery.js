 var request = new XMLHttpRequest();
    request.open('GET', 'data.json', false);
    request.send(null);
    var o = JSON.parse(request.responseText);
    var tweets = o.length - 1; //Saber nombre d'elements de l'array

    var father = document.getElementById("cd-timeline");
    console.log(father);
    var i;
    var result = "";
    for (i = tweets; i >= 0; --i) {

        var textTweet = o[i].text;
        var datetweet = o[i].time;
        var urlImage;
        if (o[i].imurl) {
            if(o[i].imurl== "null") {
                urlImage = "";
            }
            else {
                urlImage = o[i].imurl;
            }
        }
        else {
            urlImage ="";
        }




        //Parse to HTML
        var aux = "";
        var aux1 = "<div class = 'cd-timeline-img cd-picture'>";
        var aux11;

        if(urlImage != "") {
           aux11 = "<img src='images/cd-icon-picture.svg' alt='Picture'>";
        }
        else {
            aux11 = "<img src='images/bTyEekppc.png' alt='Location'>";
        }


        var aux2 = "<div class='cd-timeline-content'>";
        var aux21 = "<h2>"+ o[i].author +" - Day "+datetweet[14]+ datetweet[15] + ", " +datetweet[23] + datetweet[24]+ datetweet[25]+ datetweet[26]+datetweet[27]+"  </h2>";
        var aux22 = "<div style='padding-top: 20px;' id = 'tw-photo'><img src='" +urlImage+"' style='max-height: 400px;'></div>";
        var aux23 = "<p class='textTweet'>" + textTweet + "</p>";
        var aux24 = "<h2>RT: "+ o[i].rt + "  FAV: " + o[i].fav + "</h2>";
        if (urlImage = "") {
            aux = "<div class='cd-timeline-block' >" + aux1 + aux11 + "</div>" +
                aux2 + aux21 + aux23 +aux24 +"</div></div>";
        }
        else {
            aux = "<div class='cd-timeline-block' >" + aux1 + aux11 + "</div>" +
                aux2 + aux21 + aux22+ aux23 +aux24+"</div></div>";
        }

       result += aux;

    }
     father.innerHTML = result;


