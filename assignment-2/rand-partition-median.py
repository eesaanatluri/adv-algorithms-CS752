#!/bin/bash/env python3

import os
import sys
import math
import time
import argparse
import random
import matplotlib.pyplot as plt

#Argument parser to parse cmd line input
parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-d", required=True, help="Directory path containing data files")
args = parser.parse_args() #Array containing user given args

if args:
    path=args.dir

def partition(arr, p_idx = 0):
    i = 0
    if p_idx !=0: arr[0],arr[p_idx] = arr[p_idx],arr[0]
    for j in range(len(arr)-1):
        if arr[j+1] < arr[0]:
            arr[j+1],arr[i+1] = arr[i+1],arr[j+1]
            i += 1
    arr[0],arr[i] = arr[i],arr[0]
    return arr,i
 

def rand_select(arr, k):
    low = 0
    high = len(arr)
    # base case
    if len(arr) == 1:
        return arr[0]
    else:
        arr, idx = partition(arr, random.randrange(len(arr)))

        if idx == k:
            return arr[idx]
        elif idx > k:
            return rand_select(arr[:idx],k) # perform randomized select on first part
        else:
            k = k - idx - 1
            return rand_select(arr[(idx+1):], k) # perform randomized select on second part


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
            
            start_time = time.time() # start time

            var = rand_select(arr, len(arr)//2) # call to selection routine defined above
            print(var)
            print(f'median: {var}')
            #print(arr)
            end_time = time.time()  # end time
            exec_time = end_time-start_time

            print(f'time taken for insertion sort with {input_file} is: {exec_time}')
        
            runtime.append(exec_time) # append execution times of each dataset to the array
        print(runtime)
        
        # Graph plotting
        plt.plot([10000,20000,30000,40000,50000], runtime)
        plt.ylabel('Execution times of sorting routines')
        plt.xlabel('input size')
        plt.show()

if __name__ == "__main__":
    main()
