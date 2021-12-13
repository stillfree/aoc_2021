#!/usr/bin/env python3
import sys, time, math

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines
routes = []

def recursive( smallNum, routing, hashMap, double):
    last = routing[len(routing)-1]
    options = hashMap[last]
    for opt in options:
        if( opt != "start"):
            if( opt == "end"):
                routes.append( routing + ["end"])
            elif( opt.lower() == opt ):
                count = smallNum.count(opt)
                if( count == 0 ):
                    recursive( smallNum + [opt], routing + [opt], hashMap, double)
                elif(count == 1 and not double):
                    recursive( smallNum + [opt], routing + [opt], hashMap, True)
            elif( opt != "start" ):
                recursive( smallNum, routing + [opt], hashMap, double)

def partOne( lines ):
    hashMap = {}
    for line in lines:
        key, value = line.split("-")
        if hashMap.get(key) != None:
            hashMap[key].append(value)
        else:
            hashMap[key] = [value]
        if hashMap.get(value) != None:
            hashMap[value].append(key)
        else:
            hashMap[value] = [key]

    for option in hashMap["start"]:
        if option.lower() == option:
            recursive( [option], ["start", option], hashMap, False)
        else:
            recursive( [], ["start", option], hashMap, False)
    print(routes)
    print(len(routes))

def partTwo( lines ):
    pass

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
