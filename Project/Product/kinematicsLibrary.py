import math as m
import numpy as np
from pymycobot.mycobot import MyCobot

def toDeg(input):
    return input*180/m.pi

def TransformDesired(x,y,z,Rx,Ry,Rz):
    return np.matrix([[m.cos((m.pi*Ry)/180)*m.cos((m.pi*Rz)/180), m.cos((m.pi*Rz)/180)*m.sin((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180) - m.cos((m.pi*Rx)/180)*m.sin((m.pi*Rz)/180), m.sin((m.pi*Rx)/180)*m.sin((m.pi*Rz)/180) + m.cos((m.pi*Rx)/180)*m.cos((m.pi*Rz)/180)*m.sin((m.pi*Ry)/180), x],
                    [m.cos((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180), m.cos((m.pi*Rx)/180)*m.cos((m.pi*Rz)/180) + m.sin((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180), m.cos((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180) - m.cos((m.pi*Rz)/180)*m.sin((m.pi*Rx)/180), y],
                    [                    -m.sin((m.pi*Ry)/180),                                                                  m.cos((m.pi*Ry)/180)*m.sin((m.pi*Rx)/180),                                                                  m.cos((m.pi*Rx)/180)*m.cos((m.pi*Ry)/180), z],
                    [                                        0,                                                                                                          0,                                                                                                          0, 1]])

def CalculateThetaValues(T):
    #Theta1
    v1a = m.pi/2+m.atan2(T[1,3]-(65.5+42)*T[1,2],T[0,3]-(65.5+42)*T[0,2])+m.acos(88.78/m.sqrt((T[0,3]-(65.5+42)*T[0,2])**2+(T[1,3]-(65.5+42)*T[1,2])**2))
    v1b = m.pi/2+m.atan2(T[1,3]-(65.5+42)*T[1,2],T[0,3]-(65.5+42)*T[0,2])-m.acos(88.78/m.sqrt((T[0,3]-(65.5+42)*T[0,2])**2+(T[1,3]-(65.5+42)*T[1,2])**2))
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
        S[i,4] = m.acos((-T[1,3]*m.cos(S[i,0])+T[0,3]*m.sin(S[i,0])-88.78)/(65.5+42))

    S = np.vstack([S, S])
    for i in range(1,int(np.shape(S)[0]/2)+1):
        S[np.shape(S)[0]-i,4] = -S[np.shape(S)[0]-i,4]
    
    #Theta6
    for i in range(np.shape(S)[0]):
        S[i,5] = m.atan2((T[0,1]*m.sin(S[i,0])-T[1,1]*m.cos(S[i,0]))/m.sin(S[i,4]), (-T[0,0]*m.sin(S[i,0])+T[1,0]*m.cos(S[i,0]))/m.sin(S[i,4]))

    #Theta3
    for i in range(np.shape(S)[0]-1,-1,-1):
        P4 = np.array([T[0,3]-95*T[0,0]*m.sin(S[i,5])-95*T[0,1]*m.cos(S[i,5])-(65.5+42)*T[0,2], T[1,3]-95*T[1,0]*m.sin(S[i,5])-95*T[1,1]*m.cos(S[i,5])-(65.5+42)*T[1,2], T[2,3]-95*T[2,0]*m.sin(S[i,5])-95*T[2,1]*m.cos(S[i,5])-(65.5+42)*T[2,2]])
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
    satisfied = 0
    tempAngles = anglesDesired
    while (satisfied < 6):
        for i in range(6):
            while(True):
                print(f"{"i = "} {i} {", tempAngles[i] ="} {tempAngles[i]}")
                if (anglesDesired[i] - 0.2 < mc.get_angles()[i] < anglesDesired[i]):
                    break
                elif(anglesDesired[i] < mc.get_angles()[i] < anglesDesired[i] + 0.2):
                    break
                elif(mc.get_angles()[i] < anglesDesired[i]):
                    tempAngles[i] += 0.1
                    mc.sync_send_angles(tempAngles,5)
                elif(mc.get_angles()[i] > anglesDesired[i]):
                    tempAngles[i] -= 0.1
                    mc.sync_send_angles(tempAngles,5)
            
            satisfied += 1
    

# anglesDesired = [90,90,90,90,90,90], mc.get_angles() = [89.8,90,90,90,90,90]
# 89.8 < 89.8 < 90: false 
# 90 < 89.8 < 90.2: false
# tempAngles = [90.1,90,90,90,90,90]

# anglesDesired = [89,90,90,90,90,90], mc.get_angles() = [90,90,90,90,90,90]
# 88.8 < 90 < 89 false
# 89 < 90 < 89.2 false

# tempAngles = [89.1,90,90,90,90,90]
