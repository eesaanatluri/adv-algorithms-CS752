#!/bin/bash/env python3

import os
import sys
import math
import time
import argparse
import matplotlib.pyplot as plt

#Argument parser to parse cmd line input
parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-d", required=True, help="Directory path containing data files")
args = parser.parse_args() #Array containing user given args

if args:
    path=args.dir

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]     # We take highest idx element as the pivot
 
    for j in range(low, high):
 
        # If current element is less than or equal then swap arr[i] arr[j] 
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    # place the pivot in its place and return index
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1)
 

def quick_sort(arr, low, high):
    # base case
    if len(arr) == 1:
        return arr
    if low < high:
 
        # get partition index
        idx = partition(arr, low, high)
 
        # sort the partition upto the partitioning index
        quick_sort(arr, low, idx-1)
        # sort the partition after th partitioning index
        quick_sort(arr, idx+1, high)
 
 
def main():

    arr = []
    runtime = [] # array to plot the execution times
    #import pdb
    #pdb.set_trace()

    # Iterate through all the files in the data dir. 
    for root, dirs, files in os.walk(path):
        files.sort()
        # For each file read the i/p file as a list
        for file_name in files:
            input_file = os.path.join(root, file_name)
            with open(input_file, 'r') as f:
                for line in f.readlines():
                    arr = line.strip().split(" ")
    
            arr = list(map(int, arr)) # convert the list of strings into list of integers
            
            mid=(len(arr) - 1)//2

            start_time = time.time() # start time

            quick_sort(arr, 0, len(arr)-1) # call to sorting routine defined above

            print(f'median: {arr[mid]}')
            #print(arr)
            end_time = time.time()  # end time
            exec_time = end_time-start_time

            print(f'time taken for insertion sort with {input_file} is: {exec_time}')
        
            runtime.append(exec_time) # append execution times of each dataset to the array
        #print(runtime)
        
        # Graph plotting
        plt.plot([10000,20000,30000,40000,50000], runtime)
        plt.ylabel('Execution times of sorting routines')
        plt.xlabel('input size')
        plt.show()

if __name__ == "__main__":
    main()
