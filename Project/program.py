import math
import os
from pymycobot.mycobot import MyCobot
from Product.kinematicsLibrary import *

from pymycobot import PI_PORT, PI_BAUD
import time
from Targets import *

os.system('cls')
mc = MyCobot("COM17", 115200) #Victor
#mc = MyCobot("COM1", 115200) #Magnus

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A"],["A","A","A"],["B","B"],["B","A"]]

#sync_send_coords(home)

#mc.send_angles([0,0,0,0,0,0],20)
#print(mc.get_angles())

def runProgram(patientList):

    t = -1

    mc.sync_send_angles([0,0,0,0,0,0],25)

    mc.sync_send_coords(ApproachPillA.coords, 25, 0, 1)

    for sublist in patientList:

        print(dagPeriode[t])

        pillAmountA = sublist.count("A")
        pillAmountB = sublist.count("B") 

        t = t+1

        for x in range(pillAmountA):
            print("Picking up pill A")

            mc.sync_send_coords(ApproachPillA.coords, 25, 1, 1)
            mc.sync_send_coords(PickPillA.coords, 15, 1, 2)
            time.sleep(2)
            mc.sync_send_coords(ApproachPillA.coords, 25, 1, 1)

            ApproachPillA.update_single_coord(1, ApproachPillA.coords[1]-50)
            PickPillA.update_single_coord(1, PickPillA.coords[1]-50)
            #Update coords to pick up next pill

            mc.sync_send_coords(viapoint.coords,25,1, 1)

            mc.sync_send_coords(dayTargetsApproach[t].coords, 25, 1, 5)
            mc.sync_send_coords(dayTargetsDrop[t].coords, 25, 1, 1)
            time.sleep(2)
            mc.sync_send_coords(dayTargetsApproach[t].coords, 15, 1, 1)

            mc.sync_send_coords(viapoint.coords,25,1, 1)


        for x in range (pillAmountB):
            print("Picking up pill B")

            mc.sync_send_coords(ApproachPillB.coords, 25, 1, 1)
            mc.sync_send_coords(PickPillB.coords, 15, 1, 2)
            time.sleep(2)
            mc.sync_send_coords(ApproachPillB.coords, 25, 1, 1)

            #Update coords to pick up next pill
            ApproachPillB.update_single_coord(1, ApproachPillB.coords[1]-50)
            PickPillB.update_single_coord(1, PickPillB.coords[1]-50)

            mc.sync_send_coords(viapoint.coords,25,1, 1)
            mc.sync_send_coords(dayTargetsApproach[t].coords, 25, 1, 5)
            mc.sync_send_coords(dayTargetsDrop[t].coords, 25, 1, 1)
            time.sleep(2)
            mc.sync_send_coords(dayTargetsApproach[t].coords, 15, 1, 1)

            mc.sync_send_coords(viapoint.coords,25,1, 1)
    
        ApproachPillA.update_single_coord(0,ApproachPillA.coords[0]-50)
        ApproachPillB.update_single_coord(0,ApproachPillB.coords[0]-50)
        ApproachPillA.update_single_coord(1,-215)
        ApproachPillB.update_single_coord(1,-215)
        PickPillA.update_single_coord(0,PickPillA.coords[0]+50)
        PickPillB.update_single_coord(0,PickPillB.coords[0]+50)
        PickPillA.update_single_coord(1,-215)
        PickPillB.update_single_coord(1,-215)

        print(ApproachPillA.coords[0])


#mc.sync_send_angles([0,0,0,0,0,0],25)
#
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
#mc.sync_send_coords([-260,-15,65,180,0,0],20, 1)
#
#time.sleep(3)
#
#mc.send_coords([-260,-15,130,180,0,0],20 ,0)
# 

#mc.sync_send_angles([0,0,0,0,0,0],25)
#
#print(mc.get_coords())
#
#mc.sync_send_coords(viapoint.coords, 25, 0, 1)
#mc.sync_send_coords(ApproachPillB.coords, 25, 1, 1)
#mc.sync_send_coords(PickPillB.coords, 15, 1, 1)
#
#time.sleep(10)

runProgram(FullList)



#T = TransformDesired(-100,-250,130,180,0,0)
#S = toDeg(CalculateThetaValues(T))
#
#mc.sync_send_angles([S[0,0],S[0,1],S[0,2],S[0,3],S[0,4],S[0,5]],25)
#
#time.sleep(2)
#print(f"{"coords = "} {mc.get_coords()} {", angles ="} {mc.get_angles()}")
#
#AdjustAngles(mc, S[0,:])
#time.sleep(2)
#print(f"{"coords = "} {mc.get_coords()} {", angles ="} {mc.get_angles()}")