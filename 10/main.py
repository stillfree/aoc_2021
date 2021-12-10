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
    summer = { ")":3, "]":57, "}":1197, ">":25137 }
    summe2 = { ")":1, "]":2, "}":3, ">":4 }
    compare = { ")":"(", "]":"[", "}":"{", ">":"<" }
    compare2 = { "(":")", "[":"]", "{":"}", "<":">" }
    result = []

    valid = []
    counter = 0
    for line in lines:
        stack = []
        val = True
        for char in line:
            if char in ["(", "{", "[", "<"]:
                stack.append(char)
            else:
                curr = stack.pop()
                if( curr != compare[char] ):
                    counter += summer[char]
                    val = False
                    break
        if val:
            print(stack)
            counter2 = 0
            for i in range(len(stack)):
                counter2 *= 5
                counter2 += summe2[compare2[stack.pop()]]
            result.append(counter2)

    print(counter)
    result.sort()
    print(result[int(len(result)/2)])

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
