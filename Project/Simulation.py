from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
import kinematicsLibrary as k
import numpy as np

import program
print("hello2")
# Any interaction with RoboDK must be done through
# Robolink()

RL = robolink.Robolink()
 
# get the robot item:
robot = RL.Item('MyCoBot_320')

tool = RL.Item('End Effector')

#RL.ShowRoboDK()

home = RL.Item('home')
pillA = RL.Item('A pill')
pillB = RL.Item('B pill')
#box A targets:
pillA_app = RL.Item('pill A app')
pillA_start = RL.Item('pill A start')
pillA_end = RL.Item('pill A end')
pillA_dep = RL.Item('pill A dep')

#box B targets:
pillB_app = RL.Item('pill B app')
pillB_start = RL.Item('pill B start')
pillB_end = RL.Item('pill B end')
pillB_dep = RL.Item('pill B dep')

#Define targets needed as euler angles for moveL
#RLItem form = 'itemName'

def targetToEuler(RLitem):
    
    position = RL.item(str(RLitem)).Pose()

    print(position)

#program.runProgram([["B","A"],["A","A","B"]])

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","B"],["A","B"],["B","A"]]

#sync.send_coords(home)

print("hello")


#########################################################################################

def move_perfect_line2(startEuler, endEuler):

    startPose = k.TransformDesired(startEuler[0],startEuler[1],startEuler[2],startEuler[3],startEuler[4],startEuler[5])
    endPose = k.TransformDesired(endEuler[0],endEuler[1],endEuler[2],endEuler[3],endEuler[4],endEuler[5])

    num_steps = 100

    viapointJointsDeg = [0,0,0,0,0,0]

    for i in range(num_steps + 1):
        viapoint_pose = startPose + (endPose - startPose) * i / num_steps
        
        viapointJoints = k.CalculateThetaValues(viapoint_pose)

        print(viapointJoints)

        for i in range(5):

            viapointJointsDeg[i] = viapointJoints[0,i]*180/math.pi

        #viapointJoints2 = [viapointJoints[0,0],viapointJoints[0,1],viapointJoints[0,2],viapointJoints[0,3],viapointJoints[0,4],viapointJoints[0,5]]
        #print(viapointJointsDeg)

        viapointJointsDeg[5] = 180

        print(viapointJointsDeg[5])

        robot.MoveJ(viapointJointsDeg)

#move_perfect_line2([70,-250,80,-180,0,180], [-220, -150,80,-180,0,-180])


###########################################################################################################

#robot.MoveJ([0,0,0,0,0,0])

#print(robot.Pose())
#move_perfect_line([-126.236618, -36.785256, -104.413971, 51.199227, 90.000000, -36.236618])

def runProgram(patientList):

    t = -1

    #robot.MoveJ(home)

    for sublist in patientList:
        t = t+1
        #print(dagPeriode[t])

        pillAmountA = sublist.count("A")
        pillAmountB = sublist.count("B") 

        #robot.MoveJ(home)

        for x in range(pillAmountA):
            print("Picking up pill A")

            robot.MoveJ(pillA_app)
            robot.MoveL(pillA_start)
            robot.MoveL(pillA_end)

            #tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillA])
            #attach pill
            robot.MoveL(pillA_dep)


            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            #tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

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

            robot.MoveJ(pillB_app)
            robot.MoveL(pillB_start)
            robot.MoveL(pillB_end)

            #tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillB])
            #attach pill
            robot.MoveL(pillB_dep)

            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            #tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            #sync.send_coords(approachPillB, 25, 0)
            #sync.send_coords(pickPillB, 15, 1)

            #gripperCommand(pick)

            #sync.send_coords(approachPillB, 25, 0)
            #sync.send_coords(approachPillContainer[t], 25, 0)
            #sync.send_coords(dropPillContainter[t], 15, 1)

            #gripperCommand(drop)

            #sync.send_coords(approachPillContainer[t], 15, 1)

#runProgram(FullList)

