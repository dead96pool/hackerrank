"""

Laptop Battery Life
link: https://www.hackerrank.com/challenges/battery/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    timeCharged = float(input().strip())

    file1 = open("laptop_battery_dataset.txt","r")
    chargetime = []
    runtime = []

    data = file1.readlines()

    for line in data:
        charge, run = line.strip().split(",")
        
        chargetime.append(float(charge))
        runtime.append(float(run))

    plt.xlabel("Charge Time (Hrs)")
    plt.ylabel("Runtime (Hrs)")

    plt.scatter(chargetime,runtime)
    plt.show()

    predicted_runtime = min(timeCharged*2, 8)
    print("{:.2f}".format(predicted_runtime))