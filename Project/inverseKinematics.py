import math as m
import numpy as np

np.set_printoptions(suppress=True)

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
        if(165 >= S[i,0]*180/m.pi >= -165):
            continue
        elif (165 < S[i,0]*180/m.pi):
            print("Over 165")
            S[i,0] = S[i,0]-2*m.pi
        else:
            print("Under -165")
            S[i,0] = S[i,0]+2*m.pi

        if(195 > S[i,0]*180/m.pi > 165 or -195 < S[i,0]*180/m.pi < -165):
            print("OOB")
            S = np.delete(S, i, axis=0)



    #Theta2

    return S


T = TransformDesired(37.818805,-148.981099,523.9,90,-10,20)
#print(T)

S = CalculateThetaValues(T)
print(S*180/m.pi)

"""
[     0.925417,    -0.163176,     0.342020,    37.818805 ;
      0.336824,    -0.059391,    -0.939693,  -148.981099 ;
      0.173648,     0.984808,     0.000000,   523.900000 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];
"""

