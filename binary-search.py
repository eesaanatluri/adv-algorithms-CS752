#!/usr/bin/env python

import sys
import time
import math

def bin_search(A, key, search_first_occurence):
    #import pdb
    #pdb.set_trace()
    low=0
    high=len(A)-1
    mid=0
    result=-1
    while (low <= high):

        mid=(low + high)//2
        if A[mid].rstrip() == key:
        # If the mid element is equal to the key then search for first and last occurences
            result=mid
            if search_first_occurence:
                high=mid-1 #search left
            else:
                low=mid+1 #search right
            #return 0
            #print("found")
        if A[mid] > (key):
        # The key will be to the right if it is less than the array mid
            high = mid-1 # set new high to the element just before mid
        else:
        # The key will be to the right if it is more than the array mid 
            low = mid+1 # set new low to the element just after the mid

    return result
    #print("Not Found")

def main():

    arr=[]
    
    with open('data-1.txt', 'r') as f:
        for line in f.readlines():
            arr.append(line)
    
    start_time = time.time()
    for i in range(2, 20, 2):
        #print(str(i))
        first_hit_index = bin_search(arr, str(i), True)
        if first_hit_index == -1:
            print(f"count of {str(i)} is zero")
        else:
            last_hit_index = bin_search(arr, str(i), False)
            count = (last_hit_index - first_hit_index) + 1 
            print(f"count of {str(i)} is {count}")

    end_time = time.time()

    exec_time = end_time-start_time
    print(f'time taken for binary search: {exec_time}')

if __name__ == "__main__":
    main()
