#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def getNeighbors( x, y, limit, hashMap):
    xLimit = len(limit[0])
    yLimit = len(limit)
    returnValue = []
    result = [ [x+1, y+1], [x+1, y], [x+1, y-1], [x, y+1], [x, y-1], [x-1, y+1], [x-1, y], [x-1, y-1]]
    for res in result:
        if hashMap.get(gethashKey(res[0],res[1])) != None:
            returnValue.append(res)
    return returnValue

def gethashKey( x, y):
    return str(x)+","+str(y)

def printHash(hashMap):
    pass

def partOne( lines ):
    hashMap = {}
    for idy, line in enumerate(lines):
        for idx, octopus in enumerate(line):
            hashMap[gethashKey(idx, idy)] = [int(octopus), 0, idx, idy]
    flashCounter = 0
    step = 0
    limit = 1000
    found = False
    while( step != limit ):
        currentflashCounter = 0
        for key in hashMap.keys():
            hashMap[key][0] += 1
            #if( hashMap[key][0] > 9):
            #    print(hashMap[key][0], key)

        neighbors = []
        for key in hashMap.keys():
            value = hashMap[key]
            if( value[0] > 9 ):
                flashCounter += 1
                currentflashCounter += 1
                hashMap[key][1] = 1
                hashMap[key][0] = 0
                neighbors += getNeighbors(value[2], value[3], lines, hashMap)

        while(len(neighbors) > 0):
            neigh = neighbors.pop()
            currentKey = gethashKey(neigh[0], neigh[1])
            value = hashMap[currentKey]
            if hashMap[currentKey][1] == 0:
                hashMap[currentKey][0] += 1
                if(value[0] > 9 ):
                    currentflashCounter += 1
                    flashCounter += 1
                    hashMap[currentKey][1] = 1
                    hashMap[currentKey][0] = 0
                    neighbors += getNeighbors(value[2], value[3], lines, hashMap)

        # Reset flash
        for key in hashMap.keys():
            hashMap[key][1] = 0
        step += 1
        if currentflashCounter >= len(hashMap.keys()) and not found:
            found = True
            print("FOUND STEP:", step)

    print(flashCounter)

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    #print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
