#!/usr/bin/env python3
import sys, time, math, re

def readInput():
    if( len( sys.argv ) == 2 ):
        file = open( sys.argv[1] , "r")
    else:
        file = open("input", "r")
    lines = [ element for element in file.readlines() ]
    return lines

def checkBoard( board ):
    for i in range(5):
        if( board[0+i*5:5+i*5] == ["X","X","X","X","X"]):
            return True
        allX = True
        for j in range(5):
            if( board[i + 5*j] != "X"):
                allX = False
        if(allX):
            return True
    return False

def replaceNum(board, num):
    for i in range(len(board)):
        if( board[i] == num ):
            board[i] = "X"

def partOne( lines ):
    numbers = lines[0].rstrip().split(",")
    boardList = []
    boards = "".join(lines[2:])
    boards = boards.replace("\n", " ")
    boards = boards.replace("  ", " ")
    boards = boards.split(" ")
    boards = [ x for x in boards if x ]
    boardList = [boards[x:x+25] for x in range(0, len(boards),25)]
    for number in numbers:
        for board in boardList:
            replaceNum(board, number)
            if checkBoard(board):
                if(len(boardList) == 1 ):
                    # LastBoard
                    pass
                summe = 0
                newBoard = [ x for x in board if x != "X" ]
                for i in newBoard:
                    summe += int(i)
                print("PartOne:", int(number) * summe)
                return

def printBoard(board):
    for i in range(5):
        print(board[0+i*5:5+i*5])

def partTwo( lines ):
    numbers = lines[0].rstrip().split(",")
    print(numbers)
    boardList = []
    boards = "".join(lines[2:])
    boards = boards.replace("\n", " ").replace("  ", " ").split(" ")
    boards = [ x for x in boards if x ]
    boardList = [boards[x:x+25] for x in range(0, len(boards),25)]
    lastBoard = 0
    for number in numbers:
        toRemove = []
        remove = False
        for board in boardList:
            replaceNum(board, number)
            if checkBoard(board):
                toRemove.append([list(board), number])
                remove = True
        if remove:
            lastBoard = toRemove
            for rm in toRemove:
                boardList.remove(rm[0])
    summe = 0
    printBoard(lastBoard[0][0])
    for i in [ x for x in lastBoard[0][0] if x != "X" ]:
        summe += int(i)
    print("PartTwo:", lastBoard[0][1], int(lastBoard[0][1]) * summe)
    exit(0)

def main():
    lines = readInput()
    partOne( lines )
    partTwo( lines )


if __name__ == "__main__":
    main()
