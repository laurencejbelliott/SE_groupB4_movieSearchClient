from urllib2 import urlopen as uOpen
import json

def movieSearch(text,year,date,API):
    if API == 'OMDB':
        API_KEY = '952f2834'

        APIurl = "http://www.omdbapi.com/?apikey=" \
        + API_KEY + "&t=" + text.replace(" ","+") + "&y" \
        "=" + year
        print APIurl
        resultJSON = json.load(uOpen(APIurl))
    else:
        API_KEY = '174496bdd4390eb9d2052615c460401b'

        APIurl = "https://api.themoviedb.org/3/movie/550?api_key=174496bdd4390eb9d2052615c460401b"

    movieData = resultJSON
    return movieData

if __name__ == "__main__":
    print movieSearch("John Wick","2014",None,"OMDB")