#!/usr/bin/env python3
import sys, time, math
from collections import Counter, deque

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element.rstrip() for element in file.readlines() ]
    return lines

def partOne( lines ):
    hashMap = {}
    start = lines[0]
    for line in lines[2:]:
        A, B = line.split(" -> ")
        hashMap[A] = B
    current = start
    step = 10
    length = []
    length.append([len(current), current.count("N")])
    for i in range(step):
        temp = ""
        for i in range(len(current)-1):
            char1 = current[i]
            char2 = current[i+1]
            hashKey = char1 + char2
            #print(hashKey)
            temp += char1
            temp += hashMap[hashKey]
            #temp += char2
            #print(temp)
        temp += current[len(current)-1]
        current = temp
        length.append([len(current), current.count("N")])
        #print(current)
    second = {}
    for char in current:
        number = current.count(char)
        second[char] = number

    maxi = 0
    mini = 200000000000000
    for key in second.keys():
        num = second[key]
        if num > maxi:
            maxi = num
        elif num < mini:
            mini = num
    print("PartOne:", maxi-mini)



def partTwo( lines ):
    hashMap = {}
    start = lines[0]
    for line in lines[2:]:
        A, B = line.split(" -> ")
        hashMap[A] = B

    step = 40
    counter = Counter()
    for i in range(len(start)-1):
        counter[start[i]+start[i+1]] += 1

    for i in range(step):
        counter2 = Counter()
        for count in counter:
            counter2[count[0]+hashMap[count]] += counter[count]
            counter2[hashMap[count]+count[1]] += counter[count]
        counter = counter2

    print(counter)

    counter3 = Counter()
    for k in counter:
        counter3[k[0]] += counter[k]
    counter3[start[-1]] += 1

    print("PartTwo:", max(counter3.values())-min(counter3.values()))

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
