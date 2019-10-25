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
    return top10

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
    return totalLength/count,minMovie, maxMovie
