"""This module handles all functions related to reading and writing to files
"""
import csv


def formatTimes(seconds):
    """
    Make the lengths of the movies more user friendly
    """
    minutes, _ = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return str(hours) + "h " + str(minutes) + "m"

def readData():
    """
    Thie function will read the movieData.txt file and return
    it in dict form so that all of the information can be more easy accessed,
    the reason I used a dict as oppose to list is so that accessing movies given a title
    you don't need to do a linear search as you know the index
    Returns: 
        a dict containing the movie information
    """
    movieData = {}
    data = open("movieData.txt", "r")
    count = 0 # Used so that we dont include the first line
    categorys = []
    for x in data:
        if count != 0:
            line =  x.split(",") # Split based on commands
            movieCategorys = []
            for i in range(len(categorys)):
                if line[i+4] == "1": 
                    # Convert the 1's and 0's into valid genres
                    movieCategorys.append(categorys[i])
            movieData[line[0]] = {"rating" : line[1], "length" : line[2],"viewLength" : formatTimes(int(line[2])), "year" : line[3], "genre" : movieCategorys}
        else:
            line = x.split(",")
            categorys = line[4:len(line)]
            # This is the first line, so we create a list for the categorys
        count += 1
    return movieData

def loadUsers():
    """
    This function will create a dict of the users who are stored in the system, for this project
    there is only one but this will allow for any amount of users, it creates a dict with the index
    being the username so that accessing this is extremely fast and easy"""

    userDict = {}
    data = csv.DictReader(open("userData.csv"))
    for row in data:
        newDict = dict(row)
        movies = newDict["watchedMovies"].split("|") 
        # I used | to split the movies as commas were already being used and there might be future information such as payment info
        # that would be problematic if I used comments and just started at index 2
        newMovies = []
        for i in movies:
            if i != "" and i != " ": # Make sure it doesn't get the starting or end of the list which would be empty
                newMovies.append(i)
        userDict[newDict["id"]] = {"watchedMovies" : newMovies}
    return userDict

def getUserInfo(userName, userDict):
    """This module will return the users information, if it exists
    and if it doesn't it will create a blank one
    Parameters: 
        username
        userDict - dict containing information of all existing users
    Returns:
        a dict with the users information
    """
    if not userName in userDict:
        print("resetting users movies!")
        userDict[userName] = {"watchedMovies" : []}
    return userDict[userName]    

def saveInfo(userDict):
    """
    This function will overrwrite existing data with the new userDict and should 
    only be used when you are exiting the application as it will update any of the contents of the 
    csv file with the new information. In actual application this would not be done on a csv file but just add
    information to a database so the structure of this isn't ideal.

    Parameters:
        userDict - a dict containing the information of all users
    """
    data = csv.reader(open("userData.csv", "r"))
    newData = []
    for i in data:
        # Unable to access data[0] so need to do it this way
        newData.append(i)
        break
    for i in userDict:
        userList = []
        watchedMovies = ""
        for movie in userDict[i]["watchedMovies"]:
            watchedMovies =  watchedMovies + movie + "|"
        userList.append(i)
        userList.append(watchedMovies)    
        newData.append(userList)
    userFile =open("userData.csv", "w")    
    writer = csv.writer(userFile)    
    writer.writerows(newData)

if __name__ == "__main__":
    movieData = readData()
    #print(movieData["Hannibal "]["length"])
    print(movieData["Hannibal "]["genre"])
   # print(loadUsers())
    #print(saveInfo())
