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
    depth = 0
    forward = 0
    for line in lines:
        if( "forward" in line ):
            forward += int(line.split(" ")[1])
        elif( "up" in line ):
            depth -= int(line.split(" ")[1])
        elif( "down" in line ):
            depth += int(line.split(" ")[1])
    result = depth * forward
    print("PartOne:", result )

def partTwo( lines ):
    depth = 0
    forward = 0
    aim = 0
    for line in lines:
        if( "forward" in line ):
            value = int(line.split(" ")[1])
            forward += value
            depth += aim * value
        elif( "up" in line ):
            value = int(line.split(" ")[1])
            aim -= value
        elif( "down" in line ):
            value = int(line.split(" ")[1])
            aim += value

    result = depth * forward
    print("PartTwo:", result )

def main():
    lines = readInput()
    print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
