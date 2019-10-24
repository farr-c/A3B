def readData():
    movieData = {}
    data = open("movieData.txt", "r")
    count = 0
    for x in data:
        if count != 0:
            line =  x.split(",")
            movieData[line[0]] = {"rating" : line[1], "duration" : line[2], "year" : line[3], "genre" : line[4:(len(line))]}
        count += 1
    return movieData


if __name__ == "__main__":
    movieData = readData()
    print(movieData["Hannibal "]["genre"])