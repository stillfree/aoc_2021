#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def partOne( lines ):
    area = []
    newArea = []
    for i in range(9):
        area.append(0)
        newArea.append(0)
        area[i] = lines[0].count(str(i))
    day = 0
    while day != 256:
        newArea[0] = area[1]
        newArea[1] = area[2]
        newArea[2] = area[3]
        newArea[3] = area[4]
        newArea[4] = area[5]
        newArea[5] = area[6]
        newArea[6] = area[0] + area[7]
        newArea[7] = area[8]
        newArea[8] = area[0]
        area = list(newArea)
        day += 1
        summe = 0
        for i in range(0,9):
            summe += area[i]
        if(day == 80):
            print("PartOne:", summe)
    summe = 0
    for i in range(0,9):
        summe += area[i]
    print("PartTwo:",summe)

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    #print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
