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
    #Theta 1
    v1a = m.pi/2+m.atan2(T[1,3]-65.5*T[1,2],T[0,3]-65.5*T[0,2])+m.acos(88.78/m.sqrt((T[0,3]-65.5*T[0,2])**2+(T[1,3]-65.5*T[1,2])**2))
    v1b = m.pi/2+m.atan2(T[1,3]-65.5*T[1,2],T[0,3]-65.5*T[0,2])-m.acos(88.78/m.sqrt((T[0,3]-65.5*T[0,2])**2+(T[1,3]-65.5*T[1,2])**2))
    S = np.array([[v1a,0,0,0,0,0],[v1b,0,0,0,0,0]])

    for i in range(np.shape(S)[0]-1,-1,-1):
        if(165 >= S[i,0]*180/m.pi >= -165):
            continue
        elif (165 < S[i,0]*180/m.pi):
            #print("Over 165")
            S[i,0] = S[i,0]-2*m.pi
        else:
            #print("Under -165")
            S[i,0] = S[i,0]+2*m.pi

        if(195 > S[i,0]*180/m.pi > 165 or -195 < S[i,0]*180/m.pi < -165):
            #print("OOB")
            S = np.delete(S, i, axis=0)
    #Theta 5

    for i in range(np.shape(S)[0]):
        S[i,4] = m.acos((-T[1,3]*m.cos(S[i,0])+T[0,3]*m.sin(S[i,0])-88.78)/65.5)

    S = np.vstack([S, S])
    for i in range(1,int(np.shape(S)[0]/2)+1):
        print(i)
        S[np.shape(S)[0]-i,4] = -S[np.shape(S)[0]-i,4]
    #Theta 6
    
    for i in range(np.shape(S)[0]):
        S[i,5] = m.atan2((T[0,1]*m.sin(S[i,0])-T[1,1]*m.cos(S[i,0]))/m.sin(S[i,4]), (-T[0,0]*m.sin(S[i,0])+T[1,0]*m.cos(S[i,0]))/m.sin(S[i,4]))

    #Theta 3,2,4

    return S




T = TransformDesired(-112.044142,-200.758435,441.219650,110,-50,-10)

#print(T)

S = CalculateThetaValues(T)


def format_func(x):
    return f"{x:8.2f}"  # Adjust the width as needed

print(np.array2string(S*180/m.pi, formatter={'float_kind': format_func}))

"""
[     0.633022,    -0.768301,     0.094846,  -112.044142 ;
     -0.111619,    -0.211824,    -0.970913,  -200.758435 ;
      0.766044,     0.604023,    -0.219846,   441.219650 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];
"""

