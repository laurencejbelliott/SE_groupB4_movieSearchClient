# All of the code in this script was written in 2018 by group B4 in the University of Lincoln's Computer Science BSc
# (Hons) course's Software Engineering module.

# The 'urlopen' function from the urllib2 module is imported with the name 'uOpen'.
# This function takes a URL as a parameter and returns the data from the addressed web page as a string.
from urllib2 import urlopen as uOpen
# The 'json' object imported here parses strings of JSON formatted text, and converts the contained variables
# and values into Python variables.
import json

# This function takes the search parameters selected by the user, and passes them to the selected API as HTTP GET
# request, then reads the JSON formatted results of the HTTP request, and converts them into a dictionary where each
# key describes a different attribute of the data returned by the API about the user's query of a movie.
def movieSearch(text,year,API):

    # 'movieData' is initialised as an empty dictionary. It will later be populated with 'key:value' pairs containing
    # data about the queried movie that has been returned by the selected API. We return this variable at the functions
    # end, and it will be used by the GUI to process the user's search and display the results, so this dictionary must
    # contain all of the data necessary to facilitate those tasks for the GUI.
    movieData = {}

    # The first 'key:value' pair in movieData pair is defined as the user's choice of API for the search. 'movieData'
    # now either looks like "{'API':'OMDB'}", or "{'API':'TMDb'}".
    movieData['API'] = API


    # This code block executes if the user has chosen OMDB as the API
    if API == 'OMDB':
        # The API key is a method used by both OMDB and TMDb to vet and monitor use of their APIs. It is unique and
        # intended to be attributed to an individual or 1 group of individuals. If you are not a member of group B4 in
        # the University of Lincoln's Software Engineering Computer Science module, and want to fork this project,
        # please obtain and use your own API keys for OMDB and TMDb.
        API_KEY = '952f2834'

        # The user's search parameters are sent to the API in the form of an HTTP GET request, with the parameter names
        # and values appended to the end of the API's URL. The spaces in the search text are replaced with pluses, as
        # URLs don't contain spaces, and the API expects this.
        APIurl = "http://www.omdbapi.com/?apikey=" \
        + API_KEY + "&t=" + text.replace(" ", "+")

        # This 'if statement' adds the year attribute to the API request if it has been set by the user (not null).
        if year is not None:
            APIurl += "&y=" + year

        # The URL of the HTTP GET request is output to the console for debugging purposes.
        print(APIurl)
        # 'resultJSON' stores the JSON response from the API, as converted to Python dictionary data type by the
        # 'json.load' method.
        resultJSON = json.load(uOpen(APIurl))

        # The data attributes for the movie returned as a JSON response by the API, and converted to a Python
        # dictionary ('resultJSON') are stored under new names in the 'movieData' dictionary.
        movieData['Title'] = resultJSON['Title']
        movieData['Year'] = resultJSON['Year']
        movieData['Date'] = resultJSON['Released']
        movieData['Reviews'] = resultJSON['Ratings']
        movieData['Maturity'] = resultJSON['Rated']
        movieData['Runtime'] = resultJSON['Runtime']
        movieData['Genre'] = resultJSON['Genre']
        movieData['Cast'] = resultJSON['Actors']
        # OMDB returns both the writer(s) and director(s) as their own 'key:string' pairs. This line concatenates these
        # values into one variable and assigns it to the key 'Crew' in the 'movieData' dictionary.
        movieData['Crew'] = "\n\tWriter: " + resultJSON['Writer'] + "\n\tDirector(s): " + resultJSON['Director']
        movieData['Plot'] = resultJSON['Plot']

    # This code block executes if the user has chosen TMDb as the API, the logic is binary as there are only two choices
    # of API.
    else:
        # The API key is a method used by both OMDB and TMDb to vet and monitor use of their APIs. It is unique and
        # intended to be attributed to an individual or 1 group of individuals. If you are not a member of group B4 in
        # the University of Lincoln's Software Engineering Computer Science module, and want to fork this project,
        # please obtain and use your own API keys for OMDB and TMDb.
        API_KEY = '174496bdd4390eb9d2052615c460401b'

        # TMDb's API can return an up-to-date list of the genres used to tag movies on their site, and these genres are
        # stored in an associative array in JSON(equivalent to a Python dictionary), which contains pairs of genre IDs
        # and names. When a film's data is returned by TMDb it's genre(s) are formatted as a list of IDs, and so by
        # downloading and storing these 'id:genre' pairings in a dictionary called 'TMDbGenres', we can later use them
        # to decode the genre IDs into strings to display to the user.
        genresIDsURL = "https://api.themoviedb.org/3/genre/movie/list?api_key=" + API_KEY
        genresJSON = json.load(uOpen(genresIDsURL))['genres']

        TMDbGenres = {}
        for genre in genresJSON:
            genreID = genre['id']
            genreName = genre['name']

            TMDbGenres[str(genreID)] = genreName

        # The user's search parameters are sent to the API in the form of an HTTP GET request, with the parameter names
        # and values appended to the end of the API's URL. The spaces in the search text are replaced with pluses, as
        # URLs don't contain spaces, and the API expects this.
        APIurl = "https://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + \
                 "&query=" + text.replace(" ", "+")
        # The URL of the HTTP GET request is output to the console for debugging purposes.
        print(APIurl)
        # 'resultJSON' stores the JSON response from the API, as converted to Python dictionary data type by the
        # 'json.load' method.
        resultJSON = json.load(uOpen(APIurl))
        # The 'results' key of 'movieData' is assigned to an empty list, as TMDb can return multiple results
        # matching the user's search.
        movieData['results'] = []

        # For each result in the JSON response from the TMDb API, the movie data from that result is stored in a
        # temporary dictionary called 'resultData' and this dictionary is then appended to the results list in
        # 'movieData'.
        for result in resultJSON['results']:
            resultData = {}

            resultData['Title'] = result['title']
            # The year is taken as a substring of the 'release_date' value returned by TMDb. The release date is
            # formatted as 'yyyy-mm-dd', and so the split method of the string is called to create a list of strings
            # from the 'release_date' string, separated by the '-' character, and then the first string in the list, the
            # year, indexed by 0, is assigned to the 'Year' key of 'resultData'.
            resultData['Year'] = result['release_date'].split('-')[0]
            resultData['Date'] = result['release_date']
            resultData['Reviews'] = result['vote_average']

            # The review score returned by TMDb is an average of the site's users' ratings of a movie from 1 to 10.
            # When movies have zero user reviews the value returned is 0, and so to avoid confusing the user into
            # thinking that a movie with no reviews is instead poorly reviewed, the value for 'Reviews' in 'resultData'
            # is set to 'n/a' (not applicable).
            if resultData['Reviews'] == 0:
                resultData['Reviews'] = 'n/a'

            # The 'Genre' key is initially assigned the genre IDs returned in the JSON response from TMDb.
            resultData['Genre'] = result['genre_ids']

            # 'tempGenres' is defined as an empty list, and is then populated with the genre names stored in the
            # 'TMDbGenres' dictionary keyed by their associated genre IDs.
            tempGenres = []
            for genreID in resultData['Genre']:
                tempGenres.append(TMDbGenres[str(genreID)])

            # The list of genres is converted to a comma separated string and assigned to the 'Genre' key of
            # 'resultData'.
            tempGenresString = ', '.join(tempGenres)
            resultData['Genre'] = tempGenresString

            resultData['Plot'] = result['overview']

            # The dictionary 'resultData' generated in each iteration of the for loop is appended to the list keyed by
            # 'results' in 'movieData'.
            movieData['results'].append(resultData)
    # movieData is returned as the function's output.
    return movieData

# This function takes the dictionary 'movieData' output by the 'movieSearch' function as input, and outputs a HTML
# string. The GUI will later display and render the HTML for output to the user. This function is a work in progress.
def movieData2HTML(movieDataDict):
    if movieDataDict['API'] == 'OMDB':
        reviews = movieDataDict['Reviews']
        reviewsHTML = ""
        for review in reviews:
            reviewsHTML += """
<b>Source:</b> """ + review['Source'] + """, <b>Value: </b>""" + review['Value'] + "<br><br>"


        HTML = """
        <b>Title: """ + movieDataDict['Title'] + """</b>
        <br>
        <b>Year: """ + movieDataDict['Year'] + """</b>
        <br>
        <b>Length: """ + movieDataDict['Runtime'] + """</b>
        <br>
        <b>Genre: """ + movieDataDict['Genre'] + """</b>
        <br>
        <b>Rating: """ + movieDataDict['Maturity'] + """</b>
        <br>
        <b>Cast: """ + movieDataDict['Cast'] + """</b>
        <br>
        """ + reviewsHTML + """</b>
        """

        # Example of accessing movie data for TMDb results:

        # for result in movieDataDict['results']:
        #     result['Title']

        return HTML
    else:
        HTML = """ """

        for result in movieDataDict['results']:
            HTML = HTML + """ 
            <b>Title:</b> """ + result['Title'] + """
            <br>
            <b>Year:</b> """ + result['Year'] + """
            <br>
            <b>Genre:</b> """ + result['Genre'] + """
            <br>
            <b>Reviews:</b> """ + str(result['Reviews']) + """
            <br>
            <b>Plot:</b> """ + result['Plot'] + """
            <br>
            <br>"""

        return HTML

# This code in the scope of this 'if statement' runs if the code is executed directly, as opposed to being imported
# in another Python script. This is where the execution of the program code begins. The following code is used for
# debugging purposes and should not be included in the final version of this script.
if __name__ == "__main__":
    print("OMDB Results:\n")
    # 'OMDBResults' is assigned the movieData dictionary returned by calling 'movieSearch' with the text 'John Wick',
    # year '2014', and API 'OMDB'.
    OMDBResults = movieSearch("Dredd","2012","OMDB")

    # Empty string is printed to output an empty line to console.
    print("")

    # The key and value pairings in OMDBResults are output to the console
    for key in OMDBResults.keys():
        if str(type(OMDBResults[key])) == "<type 'unicode'>":
            print(key + ": " + OMDBResults[key])
        elif key == 'Reviews':
            print(key + ":")
            for reviewDict in OMDBResults[key]:
                for reviewKey in reviewDict.keys():
                    print("\t" + reviewKey + ": " + reviewDict[reviewKey])
                print("")
        print("")

    # An empty line followed by a string representation of the dictionary returned by 'movieSearch' are printed to the
    # console.
    print("\n", movieSearch("Dredd","2012","OMDB"))

    # 'TMDbResults' is assigned the movieData dictionary returned by calling 'movieSearch' with the text 'John Wick',
    # year '2014', and API 'TMDb'.
    print("TMDb Results:\n")
    TMDbResults = movieSearch("Dredd","2012","TMDb")

    print("")
    # The key and value pairings in TMDbResults are output to the console
    for result in TMDbResults['results']:
        for datumKey in result.keys():
            print(datumKey + ":", result[datumKey])
        print("")

    # An empty line followed by a string representation of the dictionary returned by 'movieSearch' are printed to the
    # console.
    print("\n", movieSearch("Dredd","2012", "TMDb"))


    # The raw HTML returned by 'movieData2HTML' with the dictionary returned by 'movieSearch' as a parameter is output
    # to the console. This HTML is not rendered, so does not appear is it will in the GUI. Saving it as a HTML file and
    # opening the file using an internet browser will allow you to see a rough preview of how it will appear for the
    # user in the GUI.
    print("\n")
    print(movieData2HTML(movieSearch("Dredd", "2012", "OMDB")))

    print("\n")
    print(movieData2HTML(movieSearch("Dredd", "2012", "TMDb")))