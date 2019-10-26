import csv

def formatTimes(seconds):
    minutes, _ = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return str(hours) + "h " + str(minutes) + "m"

def readData():
    movieData = {}
    data = open("movieData.txt", "r")
    count = 0
    categorys = []
    for x in data:
        if count != 0:
            line =  x.split(",")
            movieCategorys = []
            for i in range(len(categorys)):
                if line[i+4] == "1":
                    movieCategorys.append(categorys[i])
            movieData[line[0]] = {"rating" : line[1], "length" : line[2],"viewLength" : formatTimes(int(line[2])), "year" : line[3], "genre" : movieCategorys}
        else:
            line = x.split(",")
            categorys = line[4:len(line)]
        count += 1
    return movieData

def loadUsers():
    userDict = {}
    data = csv.DictReader(open("userData.csv"))
    for row in data:
        newDict = dict(row)
        movies = newDict["watchedMovies"].split("|")
        newMovies = []
        for i in movies:
            if i != "" and i != " ":
                newMovies.append(i)
        userDict[newDict["id"]] = {"watchedMovies" : newMovies}
    return userDict

def getUserInfo(userName, userDict):
    if not userName in userDict:
        print("resetting users movies!")
        userDict[userName] = {"watchedMovies" : []}
    return userDict[userName]    

def saveInfo(userDict):
    
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
