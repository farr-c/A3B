import IO

def searchMovie(movies, search):
    results = []
    movieName = ""
    for x in movies:
        if (x.lower()).find(search.lower()) != -1:
            results.append(x)
    for i in range(len(results)):
        print( str(i + 1) + ". " + results[i])

    while True:
        try:
            choice = input("\n" + str(len(results)) + " movies found, input the number which you would like to watch!")
            movieName = results[int(choice) - 1]
            break
        except:
            print("\nInvalid response! Please make sure all responses are only digits that do not exceed the search length!\n")
    
    print("you are now watching: " + movieName)

if __name__ == "__main__":
    searchMovie(IO.readData(), "han")    

    