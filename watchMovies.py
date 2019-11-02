'''
This movie handes the watching parts of the program, in real life this would be far larger
'''

def watch(userInfo, movieName):
    '''Adds the watched movie to the users watchlist
    Parameters: userInfo list of information about the user including movies they watched
    '''
    userInfo["watchedMovies"].append(movieName)