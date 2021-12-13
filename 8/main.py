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
    for line in lines:
        value = line.split("|")[1].split(" ")
        print(value)
        for element in value:
            leng = len(element)
            if leng  == 2 or leng == 7 or leng == 4 or leng == 3:
                counter += 1
    print(counter)

def partTwo( lines ):
    counter = 0
    for line in lines:
        numbers = [ "" for x in range(10)]
        left = [ x for x in line.split("|")[0].split(" ") if x ]
        right = [ x for x in line.split("|")[1].split(" ") if x ]
        for element in left:
            leng = len(element)
            if leng  == 2:
                sorted(element)
                numbers[1] = element
            elif leng == 3:
                sorted(element)
                numbers[7] = element
            elif leng == 4:
                sorted(element)
                numbers[4] = element
            elif leng == 7:
                sorted(element)
                numbers[8] = element
        oben = list(set(numbers[7]) - set(numbers[1]))[0]
        lm = set(numbers[4]) - set(numbers[1])
        save = lm
        save2 = numbers[1]
        obenrechts = set(save2)
        for element in left:
            if len(element) == 5:
                lm = lm.intersection(element)
            if len(element) == 6:
                obenrechts = obenrechts.intersection(element)
        print(lm)


        linksoben = set(set(save) - set(lm)).pop()
        mitte = lm.pop()
        numbers[0] += oben
        numbers[2] += oben
        numbers[3] += oben
        numbers[3] += numbers[1]
        numbers[5] += oben
        numbers[5] += linksoben + mitte
        numbers[6] += oben
        numbers[6] += linksoben + mitte
        numbers[9] += oben
        #print(numbers)
        print(numbers, mitte, linksoben, save)
        resultString = ""
        for num in right:
            sorted(num)
            leng = len(num)
            if( leng == 6 ):
                if(mitte not in num):
                    resultString += "0"
                elif(2 == len(set(num).intersection(set(numbers[1])))):
                    resultString += "9"
                else:
                    resultString += "6"
            elif( leng == 2 ):
                    resultString += "1"
            elif( leng == 3 ):
                    resultString += "7"
            elif( leng == 4 ):
                    resultString += "4"
            elif( leng == 7 ):
                    resultString += "8"
            elif( leng == 5 ):
                print(linksoben, num)
                if(len(set(num).intersection(set(numbers[1]))) == 2):
                    resultString += "3"
                elif(linksoben in num):
                    resultString += "5"
                else:
                    resultString += "2"
        number = int(resultString)
        print("RESULT:", resultString)
        counter += number
    print(counter)

def main():
    lines = readInput()
    #print(lines)
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
