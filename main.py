import IO
import browse
import watchMovies
import movieStatistics

username = "testUser2"



def main():

    movies = IO.readData()
    userDict = IO.loadUsers()
    userInfo = IO.getUserInfo(username, userDict)

    commands = [
        ["Get top 10 movies"],
        ["Shortest, longest and average"],
        ["Search"]
    ]

    for i in range(len(commands)):
        print(str(i+1) + ". " + commands[i][0] + "\n")

    choice = input("What would you like to do?")

    if choice == "1":

        print("The top 10 movies are: ")
        top10 = movieStatistics.getTop10(movies)
        for i in range(len(top10)):
            movieName = top10[-(i+1)]
            print(str(i+1) + ". " + movies[movieName]["rating"] + " " + movieName)
            
    elif choice == "2":

        average, shortestName, longestName = movieStatistics.getLengths(movies)
        print("The shortest movie is: " + shortestName + " with a length of " + movies[shortestName]["viewLength"])
        print("The longest movie is: " + longestName + " with a length of " + movies[longestName]["viewLength"])
        print("The average time was: " + IO.formatTimes(int(average)))

    elif choice == "3":
        search = input("Search for a movie!")
        watchedMovie, watched = browse.searchMovie(movies, search)
        if watched:
            watchMovies.watch(userInfo, watchedMovie)
    
    print(userInfo)
    
  
    
    
    print(userInfo)
    IO.saveInfo(userDict)



main()