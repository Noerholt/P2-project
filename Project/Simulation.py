from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
import inverseKinematics as IK
import numpy as np

# Any interaction with RoboDK must be done through
# Robolink()

RL = Robolink()
 
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
    
    position = RL.Item(str(RLitem)).Pose()

    x_pos = round(position[0,3],2)
    y_pos = round(position[1,3],2)
    z_pos = round(position[2,3],2)

    Rx_rad = math.atan2(position[2,1], position[2,2])
    Ry_rad = math.atan2(-position[2,0], (position[2,1]**2+position[2,2]**2)**0.5)
    Rz_rad = math.atan2(position[1,0], position[0,0])

    #Convert to degrees
    #Rounded to 2 decimals

    Rx_deg = round(math.degrees(Rx_rad),2)
    Ry_deg = round(math.degrees(Ry_rad),2)
    Rz_deg = round(math.degrees(Rz_rad),2)

    return([x_pos,y_pos,z_pos,Rx_deg,Ry_deg,Rz_deg])

viapoint = targetToEuler('viapoint')

#program.runProgram([["B","A"],["A","A","B"]])

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","B"],["A","B"],["B","A"]]

#sync.send_coords(home)


#########################################################################################

def move_perfect_line2(startEuler, endEuler):

    startPose = IK.TransformDesired(startEuler[0],startEuler[1],startEuler[2],startEuler[3],startEuler[4],startEuler[5])
    endPose = IK.TransformDesired(endEuler[0],endEuler[1],endEuler[2],endEuler[3],endEuler[4],endEuler[5])

    num_steps = 100

    viapointJointsDeg = [0,0,0,0,0,0]

    for i in range(num_steps + 1):
        viapoint_pose = startPose + (endPose - startPose) * i / num_steps
        
        viapointJoints = IK.CalculateThetaValues(viapoint_pose)

        print(viapointJoints)

        for i in range(5):

            viapointJointsDeg[i] = viapointJoints[0,i]*180/math.pi

        #viapointJoints2 = [viapointJoints[0,0],viapointJoints[0,1],viapointJoints[0,2],viapointJoints[0,3],viapointJoints[0,4],viapointJoints[0,5]]
        #print(viapointJointsDeg)

        viapointJointsDeg[5] = 180

        print(viapointJointsDeg[5])

        robot.MoveJ(viapointJointsDeg)

move_perfect_line2([70,-250,80,-180,0,180], viapoint)


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

