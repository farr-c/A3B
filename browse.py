
import IO


def askToWatch(movies, movieName):
    print("\nDetails for: " + movieName)
    print("Rating: " + str(movies[movieName]["rating"]))
    print("Length: " + str(movies[movieName]["viewLength"]))
    print("Year: " + str(movies[movieName]["year"]))
    print("Genre: " + ", ".join(movies[movieName]["genre"]))
    return movieName, input("Would you like to watch the movie? y/n \n") == "y"

def searchMovie(movies, search):
    results = []
    movieName = ""
    for x in movies:
        if (x.lower()).find(search.lower()) != -1:
            results.append(x)
    for i in range(len(results)):
        print( str(i + 1) + ". " + results[i])
    if len(results) == 0:
        print("No movies match this search!")
        return

    while True:
        try:
            choice = input("\n" + str(len(results)) + " movies found, input the number which you would like to watch!\n")
            movieName = results[int(choice) - 1]
            break
        except:
            print("\nInvalid response! Please make sure all responses are only digits that do not exceed the search length!\n")
    return askToWatch(movies, movieName)
    

def recommender(movies, userinfo):
    weights = {}
    topMovieScore = 0
    topMovie = "True Detective " # If they havent watched anything they will be recomanded the top rated movie
    for i in userinfo["watchedMovies"]:
        year = movies[i]["year"]
        for genre in movies[i]["genre"]:
            weights[genre] =  genre in weights and weights[genre] + 1 or 1
        weights[year] = movies[i]["year"] in weights and + 1 or 1
    for i in movies:
        localScore = 0
        for genre in movies[i]["genre"]:
            if genre in weights:
                localScore += weights[genre] 
        if movies[i]["year"] in weights:
            localScore += weights[movies[i]["year"]]
        if localScore > topMovieScore and not i in userinfo["watchedMovies"]:
            topMovie = i
            topMovieScore = localScore
    return askToWatch(movies, topMovie)

if __name__ == "__main__":

    #movieName, watched = searchMovie(IO.readData(), "a")
    #
    movies = IO.readData()
    userDict = IO.loadUsers()
    userInfo = IO.getUserInfo("testUser2", userDict)
    recommender(movies, userInfo)     
    pass