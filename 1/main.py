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
    counter = 0
    for i in range(len(lines)-1):
        A = int(lines[i])
        B = int(lines[i+1])
        if A < B:
            counter += 1
    print("PartOne:", counter)

def partTwo( lines ):
    lastSum = 1000000
    counter = 0
    for i in range(len(lines)-2):
        A = int(lines[i])
        B = int(lines[i+1])
        C = int(lines[i+2])
        currentSum = A+B+C
        if lastSum < currentSum:
            counter += 1
        lastSum = currentSum
    print("PartTwo:", counter)

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
