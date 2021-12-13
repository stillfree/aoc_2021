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
    dots = []
    start = True
    folding = []
    for line in lines:
        if( line != "" ):
            if(start):
                dots.append([ int(e) for  e in line.split(",")])
            else:
                folding.append(line.split(" ")[2].split("="))
        else:
            start = False
    for fold in folding:
        if fold[0] == "x":
            value = int(fold[1])
            for dot in dots:
                if value < dot[0]:
                    dot[0] = value - (dot[0] - value)
        else:
            value = int(fold[1])
            for dot in dots:
                if value < dot[1]:
                    dot[1] = value - (dot[1] - value)
        hashMap = {}
        for dot in dots:
            hashMap[str(dot[0])+","+str(dot[1])] = 1
        print(len(hashMap.keys()))
    hashMap = {}
    for dot in dots:
        hashMap[str(dot[0])+","+str(dot[1])] = 1
    print(len(hashMap.keys()))


    for i in range(50):
        for j in range(50):
            hashValue = str(i)+","+str(j)
            value = hashMap.get(hashValue)
            char = "." if value == None else "X"
            print(char, end="")
        print("")


    #print(folding)
    #print(dots)

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
