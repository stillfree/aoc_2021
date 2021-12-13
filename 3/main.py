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
    result = []
    for i in range(len(lines[0])):
        result.append(0)
    for line in lines:
        for i in range(len(line)):
            result[i] += int(line[i])
    half = int(len(lines) / 2)
    resultString = ""
    print(result,half)
    for i in range(len(result)):
        if result[i] > half:
            resultString += "1"
        else:
            resultString += "0"
    print(resultString)
    valueA = int("".join(resultString),2)
    valueB = int("".join(resultString),2) ^ int("1"*len(lines[0]),2)
    print(valueA, valueB)
    print("PartOne", valueA* valueB)

def partTwo( lines ):
    values = []
    for line in lines:
        values.append(int(line, 2))

    maxPosition = len(lines[0])
    lastString = []
    currentArray = values
    for i in range(maxPosition):
        listA = []
        listB = []
        mask = int("1" + "0"*(maxPosition-1-i),2)
        for current in currentArray:
            print(bin(mask), bin(current))
            if( current & mask > 0):
                listA.append(current)
            else:
                listB.append(current)
        print(listA, listB)
        if(len(listA) >= len(listB)):
            currentArray = listA
        else:
            currentArray = listB
        lastString = currentArray
    currentArray = values
    for i in range(maxPosition):
        listA = []
        listB = []
        mask = int("1" + "0"*(maxPosition-1-i),2)
        if(len(currentArray) == 1):
            newString = currentArray
            print(currentArray)
        for current in currentArray:
            print(bin(mask), bin(current))
            if( current & mask > 0):
                listA.append(current)
            else:
                listB.append(current)
        print(listA, listB)
        if(len(listA) < len(listB)):
            currentArray = listA
        else:
            currentArray = listB
        print(currentArray)

    print("PartTwo:", newString[0]*lastString[0])

def main():
    lines = readInput()
    #print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
