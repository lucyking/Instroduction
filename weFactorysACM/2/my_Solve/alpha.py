# -*- coding: utf-8 -*-
import sys
import os
import re
import itertools


def main():

    with open(sys.argv[1], "r") as f:
        fileContent = f.readlines()
        solveMethod(fileContent)
    exit(0)


def solveMethod(lineStacks):
    pathMap = dict()
    # print(lineStacks[0])
    M, N = re.split(r",", lineStacks[0])
    # print("M, N", M, N)
    y = 0


    for line in lineStacks[1:]:
        # print(">", line)
        curLine = re.split(r"[,\n]", line)
        for x in range(int(M)):
            pathMap[getStrIndex(x, y)] = int(curLine[x])
        y += 1

    """
    print(pathMap)
    index = 0
    for key in pathMap:
        print(key,':',pathMap[key], end=", ")
        index += 1
        if(index >= int(M)):
            print('\n')
            index = 0
    """

    for j in range(int(N)):
        for i in range(int(M)):
            pathMap[str(j)+"@" + str(i)] += getMaxNeighbour(i, j, pathMap)

    #print the last node
    print(pathMap[str(int(N)-1)+"@"+str(int(M)-1)])
    # print(pathMap)


    # for key in M
    # pathMap[getIndex(x, y)] =


def getIndex(x, y):
    return y * 10 + x

def getStrIndex(x , y):
    return str(y)+"@"+str(x)

def getMaxNeighbour(x, y, map):
    nebUp_key = str(y-1)+"@"+str(x)
    nebLeft_key = str(y)+"@"+str(x-1)
    nebLeft_val = map[nebLeft_key] if nebLeft_key in map else 0
    nebUp_val = map[nebUp_key] if nebUp_key in map else 0
    return nebLeft_val if nebLeft_val > nebUp_val else nebUp_val



if __name__ == '__main__':
    main()
