import math as m
import numpy as np
import os

np.set_printoptions(suppress=True)
os.system('cls')

def TransformDesired(x,y,z,Rx,Ry,Rz):
    return np.matrix([[m.cos((m.pi*Ry)/180)*m.cos((m.pi*Rz)/180), m.cos((m.pi*Rz)/180)*m.sin((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180) - m.cos((m.pi*Rx)/180)*m.sin((m.pi*Rz)/180), m.sin((m.pi*Rx)/180)*m.sin((m.pi*Rz)/180) + m.cos((m.pi*Rx)/180)*m.cos((m.pi*Rz)/180)*m.sin((m.pi*Ry)/180), x],
                    [m.cos((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180), m.cos((m.pi*Rx)/180)*m.cos((m.pi*Rz)/180) + m.sin((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180), m.cos((m.pi*Rx)/180)*m.sin((m.pi*Ry)/180)*m.sin((m.pi*Rz)/180) - m.cos((m.pi*Rz)/180)*m.sin((m.pi*Rx)/180), y],
                    [                    -m.sin((m.pi*Ry)/180),                                                                  m.cos((m.pi*Ry)/180)*m.sin((m.pi*Rx)/180),                                                                  m.cos((m.pi*Rx)/180)*m.cos((m.pi*Ry)/180), z],
                    [                                        0,                                                                                                          0,                                                                                                          0, 1]])

def CalculateThetaValues(T):
    #Theta1
    v1a = m.pi/2+m.atan2(T[1,3]-65.5*T[1,2],T[0,3]-65.5*T[0,2])+m.acos(88.78/m.sqrt((T[0,3]-65.5*T[0,2])**2+(T[1,3]-65.5*T[1,2])**2))
    v1b = m.pi/2+m.atan2(T[1,3]-65.5*T[1,2],T[0,3]-65.5*T[0,2])-m.acos(88.78/m.sqrt((T[0,3]-65.5*T[0,2])**2+(T[1,3]-65.5*T[1,2])**2))
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
        S[i,4] = m.acos((-T[1,3]*m.cos(S[i,0])+T[0,3]*m.sin(S[i,0])-88.78)/65.5)

    S = np.vstack([S, S])
    for i in range(1,int(np.shape(S)[0]/2)+1):
        S[np.shape(S)[0]-i,4] = -S[np.shape(S)[0]-i,4]
    
    #Theta6
    for i in range(np.shape(S)[0]):
        S[i,5] = m.atan2((T[0,1]*m.sin(S[i,0])-T[1,1]*m.cos(S[i,0]))/m.sin(S[i,4]), (-T[0,0]*m.sin(S[i,0])+T[1,0]*m.cos(S[i,0]))/m.sin(S[i,4]))

    #Theta3
    for i in range(np.shape(S)[0]-1,-1,-1):
        P4 = np.array([T[0,3]-95*T[0,0]*m.sin(S[i,5])-95*T[0,1]*m.cos(S[i,5])-65.5*T[0,2], T[1,3]-95*T[1,0]*m.sin(S[i,5])-95*T[1,1]*m.cos(S[i,5])-65.5*T[1,2], T[2,3]-95*T[2,0]*m.sin(S[i,5])-95*T[2,1]*m.cos(S[i,5])-65.5*T[2,2]])
        Pl = np.array([m.sin(S[i,0])*88.78, -m.cos(S[i,0])*88.78, 173.9])
        LPlP4 = (P4[0]-Pl[0])**2+(P4[1]-Pl[1])**2+(P4[2]-Pl[2])**2

        if(255 < m.sqrt(LPlP4) or 15 > m.sqrt(LPlP4)):
            S = np.delete(S, i, axis=0)
            continue
        else:
            S[i,2] = m.acos((LPlP4-32625)/32400)

        #Theta2
        va = m.atan((P4[2]-Pl[2])/(m.sqrt((P4[0]-Pl[0])**2+(P4[1]-Pl[1])**2)))
        vb = m.acos((3825+LPlP4)/(270*m.sqrt(LPlP4)))

        xPlP4_0 = (P4[1]-Pl[1])*m.sin(S[i,0])+(P4[0]-Pl[0])*m.cos(S[i,0])

        if(xPlP4_0 >= 0):
            S[i,1] = -m.pi/2 + va - vb
            S = np.vstack([S, S[i,:]])
            S[i,2] = -S[i,2]
            S[i,1] = -m.pi/2 + va + vb
        else:
            S[i,1] = m.pi/2 - va - vb
            S = np.vstack([S, S[i,:]])
            S[i,2] = -S[i,2]
            S[i,1] = m.pi/2 - va + vb

    #Theta4
    for i in range(np.shape(S)[0]):
        x = m.cos(S[i,1] + S[i,2])*(T[2,1]*m.cos(S[i,5]) + T[2,0]*m.sin(S[i,5])) - m.sin(S[i,1] + S[i,2])*m.cos(S[i,0])*(T[0,1]*m.cos(S[i,5]) + T[0,0]*m.sin(S[i,5])) - m.sin(S[i,1] + S[i,2])*m.sin(S[i,0])*(T[1,1]*m.cos(S[i,5]) + T[1,0]*m.sin(S[i,5]))
        y = - m.sin(S[i,1] + S[i,2])*(T[2,1]*m.cos(S[i,5]) + T[2,0]*m.sin(S[i,5])) - m.cos(S[i,1] + S[i,2])*m.cos(S[i,0])*(T[0,1]*m.cos(S[i,5]) + T[0,0]*m.sin(S[i,5])) - m.cos(S[i,1] + S[i,2])*m.sin(S[i,0])*(T[1,1]*m.cos(S[i,5]) + T[1,0]*m.sin(S[i,5]))
        
        S[i,3] = m.atan2(y,x)
        
    return S

T = TransformDesired(0,-154.28,523.9,90,0,0)

print(T)

S = CalculateThetaValues(T)
#S = np.sort(S, axis=0)

def format_func(x):
    return f"{x:8.2f}"  # Adjust the width as needed

print(np.array2string(S*180/m.pi, formatter={'float_kind': format_func}))

"""
[     0.633022,    -0.768301,     0.094846,  -112.044142 ;
     -0.111619,    -0.211824,    -0.970913,  -200.758435 ;
      0.766044,     0.604023,    -0.219846,   441.219650 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];
"""
