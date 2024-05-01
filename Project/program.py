import numpy as np
import math
import sympy as sp
from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
import time
#import targets

#sync.send_coords(home)

dagPeriode = ["morgen", "middag", "aften"]
t = -1

FullList =[["A","A","B","A"],["B","A","B"]]

for sublist in FullList:
    t = t+1
    print(dagPeriode[t])

    pillAmountA = sublist.count("A")
    pillAmountB = sublist.count("B") 

    for x in range(pillAmountA):
        print("Picking up pill A")

        #sync.send_coords(approachPillA, 25, 0)
        #sync.send_coords(pickPillA, 15, 1)
        
        #gripperCommand(pick)

        #sync.send_coords(approachPillA, 25, 0)
        #sync.send_coords(approachPillContainer[t], 25, 0)
        #sync.send_coords(dropPillContainter[t], 15, 1)

        #gripperCommand(drop)

        #sync.send_coords(approachPillContainer[t], 15, 1)
        
    for x in range (pillAmountB):
        print("Picking up pill B")

        #sync.send_coords(approachPillB, 25, 0)
        #sync.send_coords(pickPillB, 15, 1)
        
        #gripperCommand(pick)

        #sync.send_coords(approachPillB, 25, 0)
        #sync.send_coords(approachPillContainer[t], 25, 0)
        #sync.send_coords(dropPillContainter[t], 15, 1)

        #gripperCommand(drop)

        #sync.send_coords(approachPillContainer[t], 15, 1)