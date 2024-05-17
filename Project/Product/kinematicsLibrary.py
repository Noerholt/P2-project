import math as m
import numpy as np
import time
from pymycobot.mycobot import MyCobot

def ToDeg(input):
    return input*180/m.pi

def TransformDesired(Coords):
    return np.matrix([[m.cos((m.pi*Coords[4])/180)*m.cos((m.pi*Coords[5])/180), m.cos((m.pi*Coords[5])/180)*m.sin((m.pi*Coords[3])/180)*m.sin((m.pi*Coords[4])/180) - m.cos((m.pi*Coords[3])/180)*m.sin((m.pi*Coords[5])/180), m.sin((m.pi*Coords[3])/180)*m.sin((m.pi*Coords[5])/180) + m.cos((m.pi*Coords[3])/180)*m.cos((m.pi*Coords[5])/180)*m.sin((m.pi*Coords[4])/180),Coords[0]],
                    [m.cos((m.pi*Coords[4])/180)*m.sin((m.pi*Coords[5])/180), m.cos((m.pi*Coords[3])/180)*m.cos((m.pi*Coords[5])/180) + m.sin((m.pi*Coords[3])/180)*m.sin((m.pi*Coords[4])/180)*m.sin((m.pi*Coords[5])/180), m.cos((m.pi*Coords[3])/180)*m.sin((m.pi*Coords[4])/180)*m.sin((m.pi*Coords[5])/180) - m.cos((m.pi*Coords[5])/180)*m.sin((m.pi*Coords[3])/180), Coords[1]],
                    [                    -m.sin((m.pi*Coords[4])/180),                                                                  m.cos((m.pi*Coords[4])/180)*m.sin((m.pi*Coords[3])/180),                                                                  m.cos((m.pi*Coords[3])/180)*m.cos((m.pi*Coords[4])/180), Coords[2]],
                    [                                        0,                                                                                                          0,                                                                                                          0, 1]])

def CalculateThetaValues(T):
    #Theta1
    v1a = m.pi/2+m.atan2(T[1,3]-(65.5+44.5)*T[1,2],T[0,3]-(65.5+44.5)*T[0,2])+m.acos(88.78/m.sqrt((T[0,3]-(65.5+44.5)*T[0,2])**2+(T[1,3]-(65.5+44.5)*T[1,2])**2))
    v1b = m.pi/2+m.atan2(T[1,3]-(65.5+44.5)*T[1,2],T[0,3]-(65.5+44.5)*T[0,2])-m.acos(88.78/m.sqrt((T[0,3]-(65.5+44.5)*T[0,2])**2+(T[1,3]-(65.5+44.5)*T[1,2])**2))
    S = np.array([[v1a,0,0,0,0,0],[v1b,0,0,0,0,0]])

    for i in range(np.shape(S)[0]-1,-1,-1):
        if(175 >= S[i,0]*180/m.pi >= -175):
            continue
        elif (175 < S[i,0]*180/m.pi):
            S[i,0] = S[i,0]-2*m.pi
        else:
            S[i,0] = S[i,0]+2*m.pi

        if(185 > S[i,0]*180/m.pi > 175 or -185 < S[i,0]*180/m.pi < -175):
            S = np.delete(S, i, axis=0)
    
    #Theta5
    for i in range(np.shape(S)[0]):
        S[i,4] = m.acos((-T[1,3]*m.cos(S[i,0])+T[0,3]*m.sin(S[i,0])-88.78)/(65.5+44.5))

    S = np.vstack([S, S])
    for i in range(1,int(np.shape(S)[0]/2)+1):
        S[np.shape(S)[0]-i,4] = -S[np.shape(S)[0]-i,4]
    
    #Theta6
    for i in range(np.shape(S)[0]):
        S[i,5] = m.atan2((T[0,1]*m.sin(S[i,0])-T[1,1]*m.cos(S[i,0]))/m.sin(S[i,4]), (-T[0,0]*m.sin(S[i,0])+T[1,0]*m.cos(S[i,0]))/m.sin(S[i,4]))

    #Theta3
    for i in range(np.shape(S)[0]-1,-1,-1):
        P4 = np.array([T[0,3]-95*T[0,0]*m.sin(S[i,5])-95*T[0,1]*m.cos(S[i,5])-(65.5+44.5)*T[0,2], T[1,3]-95*T[1,0]*m.sin(S[i,5])-95*T[1,1]*m.cos(S[i,5])-(65.5+44.5)*T[1,2], T[2,3]-95*T[2,0]*m.sin(S[i,5])-95*T[2,1]*m.cos(S[i,5])-(65.5+44.5)*T[2,2]])
        Pl = np.array([m.sin(S[i,0])*88.78, -m.cos(S[i,0])*88.78, 173.9])
        LPlP4 = (P4[0]-Pl[0])**2+(P4[1]-Pl[1])**2+(P4[2]-Pl[2])**2

        if(255 < m.sqrt(LPlP4) or 15 > m.sqrt(LPlP4)):
            S = np.delete(S, i, axis=0)
            continue
        else:
            S[i,2] = m.acos((LPlP4-32625)/32400)

        #Theta2
        xPlP4_0 = (P4[0]-Pl[0])*m.cos(S[i,0])+(P4[1]-Pl[1])*m.sin(S[i,0])
        zPlP4_0 = P4[2]-Pl[2]

        va = m.atan2(zPlP4_0,xPlP4_0)
        vb = m.acos((3825+LPlP4)/(270*m.sqrt(LPlP4)))

        S[i,1] = va - vb - m.pi/2
        S = np.vstack([S, S[i,:]])
        S[i,2] = -S[i,2]
        S[i,1] = va + vb - m.pi/2

    #Theta4
    for i in range(np.shape(S)[0]):
        x = m.cos(S[i,1] + S[i,2])*(T[2,1]*m.cos(S[i,5]) + T[2,0]*m.sin(S[i,5])) - m.sin(S[i,1] + S[i,2])*m.cos(S[i,0])*(T[0,1]*m.cos(S[i,5]) + T[0,0]*m.sin(S[i,5])) - m.sin(S[i,1] + S[i,2])*m.sin(S[i,0])*(T[1,1]*m.cos(S[i,5]) + T[1,0]*m.sin(S[i,5]))
        y = - m.sin(S[i,1] + S[i,2])*(T[2,1]*m.cos(S[i,5]) + T[2,0]*m.sin(S[i,5])) - m.cos(S[i,1] + S[i,2])*m.cos(S[i,0])*(T[0,1]*m.cos(S[i,5]) + T[0,0]*m.sin(S[i,5])) - m.cos(S[i,1] + S[i,2])*m.sin(S[i,0])*(T[1,1]*m.cos(S[i,5]) + T[1,0]*m.sin(S[i,5]))
        S[i,3] = m.atan2(y,x)

    for i in range(np.shape(S)[0]):
        if(S[i,1]*180/m.pi < -175):
            S[i,1] += 2*m.pi
        elif (S[i,1]*180/m.pi > 175):
            S[i,1] -= 2*m.pi
        
    return S

def PrintFunction(x):
    return f"{x:8.2f}"

def PrintAngleSolution(S):
    np.set_printoptions(suppress=True)
    print(np.array2string(S*180/m.pi, formatter={'float_kind': PrintFunction}))

def AdjustAngles(mc: MyCobot, anglesDesired: list):
    tempAngles = anglesDesired.copy()
    for i in range(6):
        while not(anglesDesired[i] - 0.05 < mc.get_angles()[i] < anglesDesired[i] + 0.05):
            if(mc.get_angles()[i] < anglesDesired[i]):
                tempAngles[i] += 0.05
            else:
                tempAngles[i] -= 0.05
            mc.sync_send_angles(tempAngles,4)
    
    print(f"{'endAngles:'} {mc.get_angles()}")
    print(f"{'endCoords():'} {mc.get_coords()}")

def ChooseSolution(mc: MyCobot, S, pillType):
    for i in range(np.shape(S)[0]):
        if (pillType == "A" and S[i,0] > 0 and S[i,1] > 0 and S[i,2] > 0):
            return S[i,:]
        elif (pillType == "B" and S[i,0] < 0 and S[i,1] < 0 and S[i,2] < 0):
            return S[i,:]
    for i in range(np.shape(S)[0]):
        if (pillType == "B" and S[i,0] < 0 and S[i,1] > 0 and S[i,2] > 0):
            return S[i,:]
        elif (pillType == "A" and S[i,0] > 0 and S[i,1] > 0 and S[i,2] > 0):
            return S[i,:]    

def LinearMotionA(mc: MyCobot, endAngles, steps):
    #print(f"{'endAngles      :'} {[round(num, 2) for num in endAngles]}")
    #print(f"{'mc.get_angles():'} {[round(num, 2) for num in mc.get_angles()]}")
    startAngles = mc.get_angles()
    angleDifference = endAngles - startAngles
    stepLengths = [0,0,0,0,0,0]

    for i in range(6):
        stepLengths[i] = angleDifference[i]/steps
    #print(f"{'stepLengths    :'} {[round(num, 2) for num in stepLengths]}")

    for i in range(1,steps+1):
        mc.sync_send_angles([startAngles[0] + stepLengths[0]*i,startAngles[1] + stepLengths[1]*i,startAngles[2] + stepLengths[2]*i,startAngles[3] + stepLengths[3]*i,startAngles[4] + stepLengths[4]*i,startAngles[5] + stepLengths[5]*i],5)
    
    time.sleep(1)
    #print(f"{'endAngles      :'} {[round(num, 2) for num in mc.get_angles()]}")

def Solution(mc: MyCobot, Coords, type):
    return ChooseSolution(mc, ToDeg(CalculateThetaValues(TransformDesired(Coords))), type)

def LinearMotionP(mc: MyCobot, endPosition, steps):
    print(f"{'endPosition:  '} {[round(num, 2) for num in endPosition]}")
    startPosition = mc.get_coords()
    print(f"{'startPosition:'} {[round(num, 2) for num in startPosition]}")
    stepLengths = [0,0,0,0,0,0]

    for i in range(3):
        stepLengths[i] =  (endPosition[i] - startPosition[i])/steps
    print(f"{'stepLengths    :'} {[round(num, 2) for num in stepLengths]}")

    for i in range(1,steps+1):
        #print(f"{'PositionChange:'} {np.array(startPosition) + np.array(stepLengths)*i}")
        angles = ChooseSolution(mc, ToDeg(CalculateThetaValues(TransformDesired(np.array(startPosition) + np.array(stepLengths)*i))), "A")
        angles[5] = 0
        mc.sync_send_angles(angles,10)
    
    time.sleep(1)
    print(f"{'endAngles      :'} {[round(num, 2) for num in mc.get_angles()]}")

def move_perfect_line2(mc: MyCobot, startEuler: list, endEuler: list):

    startPose = TransformDesired(startEuler)
    endPose = TransformDesired(endEuler)

    num_steps = 50

    viapointJointsDeg = [0,0,0,0,0,0]

    for i in range(num_steps + 1):
        viapoint_pose = startPose + (endPose - startPose) * i / num_steps
        if (i > 20):
            print(f"{'viapoint_pose:'} {np.round(viapoint_pose,4)}")
        
        """
        for j in range(5):
            viapointJointsDeg[j] = viapointJoints[0,j]*180/m.pi
        print(viapointJointsDeg)
        """
        #viapointJoints2 = [viapointJoints[0,0],viapointJoints[0,1],viapointJoints[0,2],viapointJoints[0,3],viapointJoints[0,4],viapointJoints[0,5]]
        #print(viapointJointsDeg)
        viapointJointsDeg = ChooseSolution(mc, ToDeg(CalculateThetaValues(viapoint_pose)), "A")
        viapointJointsDeg[5] = 0
        print(f"{'i:'} {i} {'viapointJointsDeg:'} {[round(num, 2) for num in viapointJointsDeg]}")

        mc.sync_send_angles(viapointJointsDeg, 15)