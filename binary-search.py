#!/usr/bin/env python

import sys
import time
import math

def bin_search(A, key):
    #import pdb
    #pdb.set_trace()
    low=0
    high=len(A)-1
    mid=0
    while (low <= high):

        mid=(low + high)//2
        if A[mid].rstrip() == key:
        # If the mid element is equal to the key then just end the search
            return 0
            #print("found")
        if A[mid] > (key):
        # The key will be to the right if it is less than the array mid
            high = mid-1 # set new high to the element just before mid
        else:
        # The key will be to the right if it is more than the array mid 
            low = mid+1 # set new low to the element just after the mid

    return -1
    #print("Not Found")

def main():

    arr=[]
    
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            arr.append(line)
    
    start_time = time.time()
    for i in range(2, 100001, 2):
        #print(str(i))
        bin_search(arr, str(i))
    end_time = time.time()

    exec_time = end_time-start_time
    print(f'time taken for binary search: {exec_time}')

if __name__ == "__main__":
    main()
