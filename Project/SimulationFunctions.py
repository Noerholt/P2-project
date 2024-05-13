from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
import numpy as np
import inverseKinematics as IK
import math as m
import Simulation

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","B"]]

#sync.send_coords(home)

def runProgram(patientList):

    t = -1

    for sublist in patientList:
        t = t+1
        #print(dagPeriode[t])

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


def format_func(x):
    return f"{x:8.2f}"  # Adjust the width as needed

print(np.array2string(IK.CalculateThetaValues(IK.TransformDesired(-250, -75, 80,180,0,-180))*180/m.pi, formatter={'float_kind': format_func}))


def move_perfect_line(targetJoints):

    coordRobot = mc.get_angles()

    joints = robot.Joints().list()

    difference = targetJoints - joints

    mc.send_angles((difference/20))


