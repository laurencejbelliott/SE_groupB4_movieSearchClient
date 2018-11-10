from urllib2 import urlopen as uOpen
import json

def movieSearch(text,year,date,API):
    movieData = {}
    movieData['API'] = API

    if API == 'OMDB':
        API_KEY = '952f2834'

        APIurl = "http://www.omdbapi.com/?apikey=" \
        + API_KEY + "&t=" + text.replace(" " ,"+") + "&y" \
        "=" + year
        print APIurl
        resultJSON = json.load(uOpen(APIurl))

        movieData['Title'] = resultJSON['Title']
        movieData['Year'] = resultJSON['Year']
        movieData['Date'] = resultJSON['Released']
        movieData['Reviews'] = resultJSON['Ratings']
        movieData['Maturity'] = resultJSON['Rated']
        movieData['Runtime'] = resultJSON['Runtime']
        movieData['Genre'] = resultJSON['Genre']
        movieData['Cast'] = resultJSON['Actors']
        movieData['Crew'] = "\n\tWriter: " + resultJSON['Writer'] + "\n\tDirector(s): " + resultJSON['Director']
        movieData['Plot'] = resultJSON['Plot']

    else:
        API_KEY = '174496bdd4390eb9d2052615c460401b'

        APIurl = "https://api.themoviedb.org/3/search/movie?api_key=174496bdd4390eb9d2052615c460401b" \
                 "&query=" + text.replace(" ", "+")
        print APIurl
        resultJSON = json.load(uOpen(APIurl))
        movieData['results'] = []

        for result in resultJSON['results']:
            movieData['Title'] = result['title']
            movieData['Year'] = result['release_date'].split('-')[0]
            movieData['']

    return movieData

if __name__ == "__main__":
    print "OMDB Results:\n"
    OMDBResults = movieSearch("John Wick","2014",None,"OMDB")


    for key in OMDBResults.keys():
        if str(type(OMDBResults[key])) == "<type 'unicode'>":
            print key + ": " + OMDBResults[key]
        elif key == 'Reviews':
            print key + ":"
            for reviewDict in OMDBResults[key]:
                for reviewKey in reviewDict.keys():
                    print "\t" + reviewKey + ": " + reviewDict[reviewKey]
                print ""
        print ""

    # print "TMDb Results:\n"
    # print movieSearch("John Wick","2014",None,"TMDb")