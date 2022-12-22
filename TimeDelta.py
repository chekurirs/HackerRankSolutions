#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    timestamp1 = t1
    timestamp2 = t2
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_second1 = datetime.datetime.strptime(timestamp1,time_format)
    time_second2 = datetime.datetime.strptime(timestamp2,time_format)
    return str(int(abs((time_second1-time_second2).total_seconds())))
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input().strip()

        t2 = input().strip()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

