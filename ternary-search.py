#!/usr/bin/env python

import sys
import time
import math

def ternary_search(A, key):
    #import pdb
    #pdb.set_trace()

    low=0
    high=len(A)-1

    while (low <= high):

        mid1=low + (high-low)//3
        mid2=high - (high-low)//3

        # If the mid element is equal to the key then just end the search
        if A[mid1].rstrip() == key:
            return 0
            #print("found")
        if A[mid2].rstrip() == key:
            #print("found")
            return 0

        # Check which part the key is in
        if A[mid1] > key:
        # The key will be in part 1 i.e. from start to mid1
            high = mid1-1 # set new high to the element just before mid1
        elif A[mid2] < key: 
        # The key will be in part 3 i.e mid2 to end
            low = mid2+1 # set new low to the element just after the mid2
        else:
        # The key will in part 2 in between mid1 and mid2
            low = mid1 + 1
            high = mid2 - 1

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
        ternary_search(arr, str(i))
    end_time = time.time()

    exec_time = end_time-start_time
    print(f'time taken for ternary search: {exec_time}')

if __name__ == "__main__":
    main()
