#!/usr/bin/env python

import argparse

#Argument parser to parse cmd line input
parser = argparse.ArgumentParser()
parser.add_argument("--limit", "-n", required=True, help="fibonacci range")
args = parser.parse_args() #Array containing user given args

if args:
    n=int(args.limit)

def fibonacci(n):
    a=5
    b=6
    sum=5
    total=0
    while(a <= n):
        #print(a)
        if a%2==0:
            total += a
        sum = a + b 
        a = b
        b = sum
    print(f"total is: {total}")
fibonacci(n)
        

