#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max_sum = -10000
for i in range(len(arr)-2):
    for j in range(len(arr[0])-2):
        sum = 0
        sum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        sum += arr[i+1][j+1]
        sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        #print(sum)
        if sum > max_sum:
            max_sum = sum

print(max_sum)