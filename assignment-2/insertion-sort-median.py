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

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i=j-1

        #Compare key with each element on the left of it until an element smaller than it is found
        while i >= 0 and key < A[i] :
                A[i + 1] = A[i]
                i -= 1
        A[i + 1] = key

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

            insertion_sort(arr) # call to sorting routine defined above

            print(f'median: {arr[mid]}')
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
