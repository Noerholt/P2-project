from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations

import program
 
# Any interaction with RoboDK must be done through
# Robolink()

RL = Robolink()
 
# get the robot item:
robot = RL.Item('MyCoBot_320')

tool = RL.Item('End Effector')

RL.ShowRoboDK()

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

#program.runProgram([["B","A"],["A","A","B"]])

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","B"],["A","B"],["B","A"]]

#sync.send_coords(home)

def runProgram(patientList):

    t = -1

    #robot.MoveJ(home)

    for sublist in patientList:
        t = t+1
        print(dagPeriode[t])

        pillAmountA = sublist.count("A")
        pillAmountB = sublist.count("B") 

        #robot.MoveJ(home)

        for x in range(pillAmountA):
            print("Picking up pill A")

            robot.MoveJ(pillA_app)
            robot.MoveL(pillA_start)
            robot.MoveL(pillA_end)

            tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillA])
            #attach pill
            robot.MoveL(pillA_dep)


            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            tool.DetachAll(RL.Item('MyCobot_320 Base'))

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

            tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillB])
            #attach pill
            robot.MoveL(pillB_dep)

            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            #sync.send_coords(approachPillB, 25, 0)
            #sync.send_coords(pickPillB, 15, 1)

            #gripperCommand(pick)

            #sync.send_coords(approachPillB, 25, 0)
            #sync.send_coords(approachPillContainer[t], 25, 0)
            #sync.send_coords(dropPillContainter[t], 15, 1)

            #gripperCommand(drop)

            #sync.send_coords(approachPillContainer[t], 15, 1)

runProgram(FullList)

