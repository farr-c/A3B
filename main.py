import IO
import browse
import watchMovies
import movieStatistics

username = "testUser"

def main():

    movies = IO.readData()
    userDict = IO.loadUsers()
    userInfo = IO.getUserInfo(username, userDict)

    commands = [
        ["Get top 10 movies"],
        ["Shortest, longest and average"],
        ["Search"],
        ["Recomend a movie\n"],
        ["Quit"]
    ]

    while True:
        for i in range(len(commands)):
            print(str(i+1) + ". " + commands[i][0])

        choice = input("\nWhat would you like to do?\n")
        
        if choice == "1":

            print("The top 10 movies are: ")
            top10 = movieStatistics.getTop10(movies)
            for i in range(len(top10)):
                movieName = top10[-(i+1)]
                print(str(i+1) + ". " + movies[movieName]["rating"] + " " + movieName)
                
        elif choice == "2":

            average, shortestName, longestName = movieStatistics.getLengths(movies)
            print("The shortest movie is: " + shortestName + "with a length of " + movies[shortestName]["viewLength"])
            print("The longest movie is: " + longestName + "with a length of " + movies[longestName]["viewLength"])
            print("The average time was: " + IO.formatTimes(int(average)))

        elif choice == "3":
            search = input("Search for a movie!")
            watchedMovie, watched = browse.searchMovie(movies, search)
            if watched:
                watchMovies.watch(userInfo, watchedMovie)
        elif choice == "4":
           watchedMovie, watched = browse.recommender(movies, userInfo)
           if watched:
               watchMovies.watch(userInfo, watchedMovie )
        elif choice == "5":
            print("Saving and exiting application!")
            break
        else:
            print("\n Invalid input please try again!")
        
    print(userInfo)
    IO.saveInfo(userDict)



main()