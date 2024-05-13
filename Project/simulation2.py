from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
import inverseKinematics as IK
import numpy as np

# Any interaction with RoboDK must be done through
# Robolink()

RL = Robolink()
 
# get the robot item:
robot = RL.Item('MyCoBot_320')

tool = RL.Item('Endefffector Assembled')

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

#RL.ShowRoboDK()

pillA = RL.Item('pill A start')
pillAapp = targetToEuler('pill A start app')
pillB = [RL.Item('pill B start')]
pillBapp = [RL.Item('pill B start app')]

#Define targets needed as euler angles for moveL
#RLItem form = 'itemName'


viapoint = targetToEuler('viapoint')

print(viapoint)

#program.runProgram([["B","A"],["A","A","B"]])

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","B","A"],["B","A","A"],["A","B"],["B","A"]]

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

        #print(viapointJoints)

        for i in range(5):

            viapointJointsDeg[i] = viapointJoints[0,i]*180/math.pi

        #viapointJoints2 = [viapointJoints[0,0],viapointJoints[0,1],viapointJoints[0,2],viapointJoints[0,3],viapointJoints[0,4],viapointJoints[0,5]]
        #print(viapointJointsDeg)

        viapointJointsDeg[5] = 180

        #print(viapointJointsDeg[5])

        robot.MoveJ(viapointJointsDeg)

#move_perfect_line2([70,-250,80,-180,0,180], viapoint)


###########################################################################################################

#robot.MoveJ([0,0,0,0,0,0])

#print(robot.Pose())
#move_perfect_line([-126.236618, -36.785256, -104.413971, 51.199227, 90.000000, -36.236618])

def runProgram(patientList):

    t = -1

    #robot.MoveJ(home)

    for sublist in patientList:
        pillAapp[1] = -230
        t = t+1
        #print(dagPeriode[t])

        pillAmountA = sublist.count("A")
        pillAmountB = sublist.count("B") 

        #robot.MoveJ(home)

        for x in range(pillAmountA):
            #print("Picking up pill A")

            #robot.MoveJ(pillTargetsA[x])

            #tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillA])
            #attach pill

            #print(pillAapp)

            pillAapp[1] = pillAapp[1] - 20

            #print(pillAapp[1])

            T = IK.TransformDesired(pillAapp[0],pillAapp[1],pillAapp[2],pillAapp[3],pillAapp[4],pillAapp[5])

            #print(T)

            Thetas = IK.CalculateThetaValues(T)

            print([IK.toDeg(Thetas[0][0]), IK.toDeg(Thetas[0][1]), IK.toDeg(Thetas[0][2]), IK.toDeg(Thetas[0][3]), IK.toDeg(Thetas[0][4]), IK.toDeg(Thetas[0][5])])

            robot.MoveJ([IK.toDeg(Thetas[0][0]), IK.toDeg(Thetas[0][1]), IK.toDeg(Thetas[0][2]), IK.toDeg(Thetas[0][3]), IK.toDeg(Thetas[0][4]), IK.toDeg(Thetas[0][5])])

            robot.MoveJ(RL.Item('viapoint'))

        for x in range (pillAmountB):
            #print("Picking up pill B")


            #tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillB])
            #attach pill

            #robot.moveJ(pillTargetsB[x])

            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            #tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))


B = IK.TransformDesired(-50,-250,50,-180,0,180)

C = IK.CalculateThetaValues(B)

def format_func(x):
    return f"{x:8.2f}"  # Adjust the width as needed

print(np.array2string(C*180/math.pi, formatter={'float_kind': format_func}))

print(C[0][0]*180/math.pi)

robot.MoveJ([C[0][0]*180/math.pi,C[0][1]*180/math.pi,C[0][2]*180/math.pi,C[0][3]*180/math.pi,C[0][4]*180/math.pi,C[0][5]*180/math.pi])

#runProgram(FullList)
