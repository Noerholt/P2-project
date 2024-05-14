from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
from kinematicsLibrary import *
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

pillA = targetToEuler('pill A start')
pillAapp = targetToEuler('pill A start app')
pillB = targetToEuler('pill B start')
pillBapp = targetToEuler('pill B start app')

#Define targets needed as euler angles for moveL
#RLItem form = 'itemName'


viapoint = targetToEuler('viapoint')

print(viapoint)

#program.runProgram([["B","A"],["A","A","B"]])

dagPeriode = ["morgen", "middag", "aften", "nat"]

FullList =[["A","A","A","A"],["B","B","B"],["B","B"],["B","A"]]

#sync.send_coords(home)


#########################################################################################

def move_perfect_line2(startEuler, endEuler):

    startPose = TransformDesired(startEuler[0],startEuler[1],startEuler[2],startEuler[3],startEuler[4],startEuler[5])
    endPose = TransformDesired(endEuler[0],endEuler[1],endEuler[2],endEuler[3],endEuler[4],endEuler[5])

    num_steps = 100

    viapointJointsDeg = [0,0,0,0,0,0]

    for i in range(num_steps + 1):
        viapoint_pose = startPose + (endPose - startPose) * i / num_steps
        
        viapointJoints = CalculateThetaValues(viapoint_pose)

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
        pillA[1] = -230
        pillBapp[1] = -230
        pillB[1] = -230
        print(pillBapp)
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
            pillA[1] = pillA[1] - 20

            T_Aapp = TransformDesired(pillAapp[0],pillAapp[1],pillAapp[2],pillAapp[3],pillAapp[4],pillAapp[5])
            T_A = TransformDesired(pillA[0],pillA[1],pillA[2],pillA[3],pillA[4],pillA[5])

            #print(T)

            ThetasAapp = CalculateThetaValues(T_Aapp)
            ThetasA = CalculateThetaValues(T_A)

            robot.MoveJ([toDeg(ThetasAapp[0][0]), toDeg(ThetasAapp[0][1]), toDeg(ThetasAapp[0][2]), toDeg(ThetasAapp[0][3]), toDeg(ThetasAapp[0][4]), toDeg(ThetasAapp[0][5])])

            robot.MoveL([toDeg(ThetasA[0][0]), toDeg(ThetasA[0][1]), toDeg(ThetasA[0][2]), toDeg(ThetasA[0][3]), toDeg(ThetasA[0][4]), toDeg(ThetasA[0][5])])

            robot.MoveL([toDeg(ThetasAapp[0][0]), toDeg(ThetasAapp[0][1]), toDeg(ThetasAapp[0][2]), toDeg(ThetasAapp[0][3]), toDeg(ThetasAapp[0][4]), toDeg(ThetasAapp[0][5])])

            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            #tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

        for x in range (pillAmountB):
            #print("Picking up pill B")


            #tool.AttachClosest(keyword='', tolerance_mm=-2,list_objects=[pillB])
            #attach pill

            #robot.moveJ(pillTargetsB[x])

            pillBapp[1] = pillBapp[1] - 20
            pillB[1] = pillB[1] - 20

            T_Bapp = TransformDesired(pillBapp[0],pillBapp[1],pillBapp[2],pillBapp[3],pillBapp[4],pillBapp[5])
            T_B = TransformDesired(pillB[0],pillB[1],pillB[2],pillB[3],pillB[4],pillB[5])

            #print(T)

            ThetasBapp = CalculateThetaValues(T_Bapp)
            ThetasB = CalculateThetaValues(T_B)

            robot.MoveJ([toDeg(ThetasBapp[0][0]), toDeg(ThetasBapp[0][1]), toDeg(ThetasBapp[0][2]), toDeg(ThetasBapp[0][3]), toDeg(ThetasBapp[0][4]), toDeg(ThetasBapp[0][5])])

            robot.MoveL([toDeg(ThetasB[0][0]), toDeg(ThetasB[0][1]), toDeg(ThetasB[0][2]), toDeg(ThetasB[0][3]), toDeg(ThetasB[0][4]), toDeg(ThetasB[0][5])])

            robot.MoveJ([toDeg(ThetasBapp[0][0]), toDeg(ThetasBapp[0][1]), toDeg(ThetasBapp[0][2]), toDeg(ThetasBapp[0][3]), toDeg(ThetasBapp[0][4]), toDeg(ThetasBapp[0][5])])

            robot.MoveL(RL.Item('viapoint'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))

            robot.MoveL(RL.Item(dagPeriode[t]))

            #tool.DetachAll(RL.Item('MyCobot_320 Base'))

            robot.MoveL(RL.Item(dagPeriode[t]+" app"))


B = TransformDesired(-250, 15, 80, 180, 0, -180)

C = CalculateThetaValues(B)

def format_func(x):
    return f"{x:8.2f}"  # Adjust the width as needed

#print(np.array2string(C*180/math.pi, formatter={'float_kind': format_func}))

#print(C[0][0]*180/math.pi)

#robot.MoveJ([C[0][0]*180/math.pi,C[0][1]*180/math.pi,C[0][2]*180/math.pi,C[0][3]*180/math.pi,C[0][4]*180/math.pi,C[0][5]*180/math.pi])

runProgram(FullList)

