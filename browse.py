
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
            choice = input("\n" + str(len(results)) + " movies found, input the number which you would like to watch!")
            movieName = results[int(choice) - 1]
            break
        except:
            print("\nInvalid response! Please make sure all responses are only digits that do not exceed the search length!\n")
    
    print("Details for: " + movieName)
    print("Rating: " + str(movies[movieName]["rating"]))
    print("Length: " + str(movies[movieName]["viewLength"]))
    print("Genre: " + ", ".join(movies[movieName]["genre"]))
    return movieName, input("Would you like to watch the movie? y/n \n") == "y"

if __name__ == "__main__":

    #movieName, watched = searchMovie(IO.readData(), "a")    
    pass