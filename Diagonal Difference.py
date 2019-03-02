#!/bin/python3

import os
# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    prim =0
    sec=0
    length = len(arr[0])
    i=0
    for cont in range(length):
        prim += arr[cont][cont]
        sec += arr[cont][(length-cont-1)]
    return abs(prim-sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()