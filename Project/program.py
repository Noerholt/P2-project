import math
from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
import time
from Targets import *

mc = MyCobot("COM17", 115200)

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","B"]]

#sync_send_coords(home)

#mc.send_angles([0,0,0,0,0,0],20)
#print(mc.get_angles())

def runProgram(patientList):

    t = 0

    mc.sync_send_angles([0,0,0,0,0,0],25)

    for sublist in patientList:

        print(dagPeriode[t])

        pillAmountA = sublist.count("A")
        pillAmountB = sublist.count("B") 

        for x in range(pillAmountA):
            print("Picking up pill A")

            mc.sync_send_coords(ApproachPillA, 25, 0)
            mc.sync_send_coords(PickPillA, 15, 1)
            time.sleep(2)
            mc.sync_send_coords(ApproachPillA, 25, 1)

            mc.sync_send_coords(viapoint,25,1)

            mc.sync_send_coords(dayTargetsApproach[t].coords, 25, 1)
            mc.sync_send_coords(dayTargetsDrop[t].coords, 25, 1)
            time.sleep(2)
            mc.sync_send_coords(dayTargetsApproach[t], 15, 1)

            t = t+1

        for x in range (pillAmountB):
            print("Picking up pill B")

            mc.sync_send_coords(ApproachPillB, 25, 0)
            mc.sync_send_coords(PickPillB, 15, 1)
            time.sleep(2)
            mc.sync_send_coords(ApproachPillB, 25, 1)

            mc.sync_send_coords(viapoint,25,1)
            mc.sync_send_coords(dayTargetsApproach[t].coords, 25, 1)
            mc.sync_send_coords(dayTargetsDrop[t].coords, 25, 1)
            time.sleep(2)
            mc.sync_send_coords(dayTargetsApproach[t], 15, 1)

            t = t+1

mc.sync_send_angles([0,0,0,0,0,0],25)

#mc.sync_send_coords([-110,-263,130,180,0,0],20,0)
#
#mc.sync_send_coords([-110,-263,44,180,0,0],20,1)
#
#time.sleep(2)
#
#mc.send_coords([-110,-263,130,180,0,0],20,0)
#
#mc.send_coords([-260,-15,130,180,0,0],20 ,0)
#
#mc.send_coords([-260,-15,65,180,0,0],20, 1)

#print(mc.get_coords())

#runProgram(FullList)