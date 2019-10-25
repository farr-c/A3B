import IO

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

def getTop10(movies):
    top10 = []
    ratings = []
    for i in movies:
        if len(ratings) < 10:
            top10.append(i)
            ratings.append(movies[i]["rating"])
            ratings.sort()
        elif movies[i]["rating"] > ratings[9]:
            for movieName in top10:
                if movies[movieName]["rating"] < movies[i]["rating"]:
                    top10.remove(movieName)
                    top10.append(i)
                    break 
                ratings[9] = movies[i]["rating"]
                ratings.sort()
    return(top10)

def getLengths(movies):
    minLength = 99999
    minMovie = ""
    maxLength = 0
    maxMovie = ""
    totalLength = 0
    count = 0
    for i in movies:
        length = int(movies[i]["length"])
        if length < minLength:
            minLength = length
            minMovie = i
        if length > maxLength:
            maxLength = length
            maxMovie = i 
        count += 1
        totalLength += length
    print(str(minLength) + " " + str(maxLength) + " " + str(totalLength//count))

if __name__ == "__main__":
    movies = IO.readData()
    getLengths(movies)
    top10 =getTop10(movies) 

    for i in top10:
        print(i + ": " + movies[i]["rating"])
    
    #movieName, watched = searchMovie(IO.readData(), "a")    
    