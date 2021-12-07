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
    crabs = [ int(e) for e in lines[0].split(",")]
    minSum = [100000000, 0]
    for i in range(0,max(crabs)):
        summe = 0
        for crab in crabs:
            summe += abs( crab - i )
        if( summe < minSum[0]):
            minSum = [summe, i]
    print(minSum)




def partTwo( lines ):
    crabs = [ int(e) for e in lines[0].split(",")]
    minSum = [10000000000000, 0]
    for i in range(0,max(crabs)):
        summe = 0
        for crab in crabs:
            counter = 0
            for j in range(1, abs( crab - i )+1):
                summe += j
        if( summe < minSum[0]):
            minSum = [summe, i]
    print(minSum)

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
