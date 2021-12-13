#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def printBasin(basin, lines):
    xList = []
    yList = []
    print(basin)
    for key in basin[4].keys():
        value = [ int(e) for e in key.split(",")]
        xList.append(value[0])
        yList.append(value[1])
    keyList = basin[4].keys()

    minX = min(yList)
    minX = minX - 1 if minX - 1 >= 0 else minX

    maxX = max(yList)
    maxX = maxX+2 if maxX + 2 < len(lines[0]) else maxX + 1

    minY = min(xList)
    minY = minY - 1 if minY - 1 >= 0 else minY

    maxY = max(xList)
    maxY = maxY+2 if maxY + 2 < len(lines) else maxY + 1

    print(minX, maxX)
    print(minY, maxY)
    for y in range(minY, maxY):
        for x in range( minX, maxX):
            char = "X" if x == basin[y] and y == basin[0] else  str(lines[y][x])
            print(char, end="")
        print("")

def getNeighbours( x, y, hashMap ):
    temp = [[x+1, y], [x-1, y], [x, y+1], [x, y-1] ]
    result = []
    for x in temp:
        if hashMap.get(getHashkey(x[0], x[1])) != None:
            result.append( x )
    return result

def getHashkey( x, y):
    return str(x) + "," + str(y)

def partOne( lines ):
    counter = 0
    basins = []
    hashMap = {}
    for idx, line in enumerate(lines):
        for idy, value in enumerate(line):
            value = int(value)
            hashKey = getHashkey(idx, idy)
            hashMap[hashKey] = value
            oben = 9 if idx-1 < 0 else lines[idx-1][idy]
            unten = 9 if idx+1 >= len(lines)  else lines[idx+1][idy]
            left = 9 if idy-1 < 0 else lines[idx][idy-1]
            right =9 if idy+1 >= len(line) else lines[idx][idy+1]
            Lowest = True
            for i in [ int(e) for e in [oben, unten, left, right]]:
                if i <= value:
                    Lowest = False
            if Lowest:
                counter += value + 1
                basins.append([idx,idy])
                #print(idx, idy)
    print("PartOne:", counter)

    counter = 0
    for basin in basins:
        idx, idy = basin
        counter = 1
        jobList = getNeighbours(idx, idy, hashMap)
        started = [[idx, idy]]
        #print("Start", basin, started)
        while(len(jobList) > 0):
            #print(len(jobList), jobList)
            element = jobList.pop(0)
            elementValue = hashMap[getHashkey(element[0], element[1])]
            if(elementValue == 9):
                continue
            if not [element[0], element[1]] in started:
                started.append([element[0], element[1]])
            neighbors = getNeighbours(element[0], element[1], hashMap)
            #print("Element:", element)
            for nb in neighbors:
                neighValue = hashMap[getHashkey(nb[0], nb[1])]
                if neighValue != 9 and not [nb[0], nb[1]] in started:
                    #print("ADDING:", neighValue, nb)
                    jobList.append([nb[0], nb[1]])
                    counter += 1
        basin.append(len(started))

    liste = []
    for b in basins:
        liste.append(b[2])
    liste.sort()
    liste = liste[::-1]
    print(liste)

    summe = liste[0]
    summe *= liste[1]
    summe *= liste[2]
    print("PartTwo:", summe)

def main():
    lines = readInput()
    partOne( lines )

if __name__ == "__main__":
    main()
