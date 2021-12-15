#!/usr/bin/env python3
import sys, time, math
sys.setrecursionlimit(20000)

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines


globalres = []

def getNeighbors( x, y, value, maxX, maxY):
    result = []
    if(y + 1 <= maxY ):
        result.append( [x, y+1, value])
    #up
    if(y - 1 >= 0 ):
        result.append( [x, y-1, value])
    #right
    if( x + 1 <= maxX ):
        result.append( [x + 1, y, value ])
    #left
    if( x - 1  >=  0 ):
        result.append( [x - 1, y, value ])
    return result

def recursive(x, y, value, goalX, goalY, maps, start):
    divider = (goalX+1)/5
    value += int(maps[x][y][0])
        #print("Not Start")
    if value < maps[x][y][1]:
        maps[x][y][1] = value
        if x == goalX and y == goalY :
            globalres.append(value)
            return
        #down
def getHashKey(x,y):
    return str(x)+","+str(y)

def partOne( lines ):
    maps = []
    for j in range(0,5):
        for line in lines:
            values = []
            for i in range(0,5):
                for char in line:
                    num = (i+j+int(char))%9 if i+j+int(char) > 9 else (i+j+int(char))
                    values.append([num, 1000000000000])
            maps.append(values)

    maxX = len(maps[0])-1
    maxY = len(maps)-1
    print(maps[maxX][maxY])
    #down
    positions = {"1,0":[1,0,0], "0,1":[0,1,0]}


    while(len(positions) > 0):
        #print(len(positions))#print(positions))
        #print(positions, list(positions.keys()))
        pos = positions.pop(list(positions.keys())[0])
        if( maps[pos[0]][pos[1]][1] > pos[2] ):
            maps[pos[0]][pos[1]][1] = pos[2]
            #print(pos, len(positions))#print(positions))
            #print(pos)
            value = pos[2] + maps[pos[0]][pos[1]][0]
            for neigh in getNeighbors(pos[0],pos[1], value, maxX, maxY):
                x = neigh[0]
                y = neigh[1]
                hashKey = getHashKey( x, y)
                if positions.get(hashKey) != None:
                    if positions[hashKey][2] > neigh[2]:
                        positions[hashKey] = [x, y, neigh[2]]
                else:
                    positions[hashKey] = [x, y, neigh[2]]

    #print(globalres, goalX, goalY)
    #print(globalres)
    #print(min(globalres))

    print(maps[maxX][maxY][1]+ maps[maxX][maxY][0] )


def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
