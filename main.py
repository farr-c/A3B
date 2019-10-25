import IO
import browse
import watchMovies

username = "testUser2"

def main():
    movies = IO.readData()
    userDict = IO.loadUsers()
    userInfo = IO.getUserInfo(username, userDict)
    search = input("debug search")
    print(userInfo)
    watchedMovie, watched = browse.searchMovie(movies, search)
    if watched:
        watchMovies.watch(userInfo, watchedMovie)
    print(userInfo)
    IO.saveInfo(userDict)


main()