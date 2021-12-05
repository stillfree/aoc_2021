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
    mappy = {}
    for line in lines:
        A, B = line.split("->")
        A = A.replace(" ","")
        B = B.replace(" ","")
        A = A.split(",")
        B = B.split(",")
        print(A,B)
        x1 = int(A[0])
        x2 = int(A[1])
        y1 = int(B[0])
        y2 = int(B[1])
        print(x1,x2,y1,y2)
        if( x1 == y1 ):
            value = [x2, y2 ]
            value.sort()
            for i in range(value[0], value[1]+1):
                hashString = A[0] + "," + str(i)
                print(hashString)
                if( hashString in mappy.keys() ):
                    mappy[hashString][0] += 1
                else:
                    mappy[hashString] = [1,0]
        elif( x2 == y2 ):
            value = [x1, y1 ]
            value.sort()
            for i in range(value[0], value[1]+1):
                hashString = str(i) + "," + A[1]
                print(hashString)
                if( hashString in mappy.keys() ):
                    mappy[hashString][0] += 1
                else:
                    mappy[hashString] = [1,0]
        else:
            print("A,B:",A,B)
            if x1 > y1:
                rangeA = list(range(x1, y1-1, -1))
            else:
                rangeA = list(range(x1, y1+1, 1))
            if x2 > y2:
                rangeB = list(range(x2, y2-1, -1))
            else:
                rangeB = list(range(x2, y2+1, 1))
            liste = list(zip(rangeA, rangeB))
            print(liste)
            for element in liste:
                hashString = str(element[0]) + "," + str(element[1])
                if( hashString in mappy.keys() ):
                    mappy[hashString][1] += 1
                else:
                    mappy[hashString] = [0,1]

    counter = 0
    counter2 = 0
    for key in mappy.keys():
        if mappy[key][0] > 1:
            counter += 1
        if mappy[key][0] + mappy[key][1] > 1:
            counter2 += 1
    print("PartOne", counter)
    print("PartTwo", counter2)


def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
