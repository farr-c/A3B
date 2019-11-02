'''This module handles all functions related to browsing 
for movies'''
import IO


def showDetails(movies, movieName):
    '''Will print out the details of a specific movie
    Parameters: 
        movies, list of the movies to be printed
        movieName, the specific movie we are printing the details for
    '''

    print("\nDetails for: " + movieName)
    print("Rating: " + str(movies[movieName]["rating"]))
    print("Length: " + str(movies[movieName]["viewLength"]))
    print("Year: " + str(movies[movieName]["year"]))
    print("Genre: " + ", ".join(movies[movieName]["genre"]))
 

def searchMovie(movies, search):
    '''This module will search through all the movies
    to find a matching result, it will then let the user pick
    one of the selected movies, it also verifies that their input is valid (must be a digit to select)

    Parameters: 
        movies - list of all the movies
        search - the string you're looking for in the movie titles
    Returns:
        the movie (if any)
        if they watched decided to watch the movie or not

    '''
    results = []
    movieName = ""
    for x in movies:
        if (x.lower()).find(search.lower()) != -1:
            results.append(x)
    for i in range(len(results)):
        print( str(i + 1) + ". " + results[i])
    if len(results) == 0:
        print("No movies match this search!")
        return "nomatch", False

    while True:
        try:
            choice = input("\n" + str(len(results)) + " movies found, input the number which you would like to watch!\n")
            movieName = results[int(choice) - 1]
            break
        except:
            print("\nInvalid response! Please make sure all responses are only digits that do not exceed the search length!\n")
    showDetails(movies, movieName)
    return movieName, input("Would you like to watch the movie? y/n \n") == "y"
    

def recommender(movies, userinfo):
    '''
    This function will recommend new movies based on what the person has watched,
    to make this decision it uses the persons favourite genres as well as the year 
    the movie was published to make a decision as I find these to be the most relevent to
    the search, another thing that could be used is rating but I didn't use it because I felt
    like the best results would be purely based on the users preferences of movies. 

    The function works by building up scores of every single movie and then picking the movie with the highest score.
    If a person doesn't want to watch a recommendation, you can skip it and it won't be recommended unless
    you leave and then re enter the recommender.

    Parameters: 
        movies - list of movies
        userInfo - a dict of information related to the user
    '''

    weights = {}
    skippedMovies = []
   
    for i in userinfo["watchedMovies"]:
        # Store the most watched movies genres and years to make score most relevent
        year = movies[i]["year"]
        for genre in movies[i]["genre"]:
            weights[genre] =  genre in weights and weights[genre] + 1 or 1
        weights[year] = movies[i]["year"] in weights and + 1 or 1


    while True:
        topMovieScore = 0
        topMovie = "True Detective " # If they havent watched anything they will be recomanded the top rated movie
        for i in movies:
            localScore = 0
            for genre in movies[i]["genre"]:
                if genre in weights:
                    localScore += weights[genre] 
            if movies[i]["year"] in weights:
                localScore += weights[movies[i]["year"]]
            if localScore > topMovieScore and not i in userinfo["watchedMovies"] and not i in skippedMovies:
                # This movie is the new highest so update the values
                topMovie = i
                topMovieScore = localScore
        showDetails(movies, topMovie)
        choice = input("\nWould you like to watch, skip this movie, or return? (watch, skip, return)\n")
        if choice == "watch":
            return topMovie, True # Person chose to watch this movie
        elif choice == "skip":
            skippedMovies.append(topMovie) # Add to a list of movies not to look for anymore
        else:
            return topMovie, False # Person would like to return to the movie


if __name__ == "__main__":

    #movieName, watched = searchMovie(IO.readData(), "a")
    #
    movies = IO.readData()
    userDict = IO.loadUsers()
    userInfo = IO.getUserInfo("testUser2", userDict)
    recommender(movies, userInfo)     
    pass