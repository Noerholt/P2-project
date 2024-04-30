import numpy as np
import math
import sympy as sp

# Define symbols
alpha, a, d, theta = sp.symbols('alpha a d theta')
theta1, theta2, theta3, theta4, theta5, theta6 = sp.symbols('theta1 theta2 theta3 theta4 theta5 theta6')


#Function to determine DH transformation matrices

def TDH(alpha, a, d, theta):
    return sp.Matrix([
        [sp.cos(theta), -sp.sin(theta), 0, a],
        [sp.sin(theta)*sp.cos(alpha), sp.cos(theta)*sp.cos(alpha), -sp.sin(alpha), -sp.sin(alpha)*d],
        [sp.sin(theta)*sp.sin(alpha), sp.cos(theta)*sp.sin(alpha), sp.cos(alpha), sp.cos(alpha)*d],
        [0, 0, 0, 1]
    ])

#Determine DH transformation matrices

T01 = TDH(0, 0, 173.9, theta1)
T12 = TDH(math.pi/2,0,0,theta2 - math.pi/2)
T23 = TDH(0, -135, 0, theta3)
T34 = TDH(0, -120, 88.78, theta4 - math.pi/2)
T45 = TDH(math.pi/2, 0, 95, theta5)
T56 = TDH(-math.pi/2, 0, 65.5, theta6)

#Define T06 transformation matrix

T06 = T01*T12*T23*T34*T45*T56

#Forward kinematics function
#Calculate position and orientation from theta values

def forward_kinematics(t1, t2, t3, t4, t5, t6) :

    """Get end effector coordinates in relation to base

        args: 
            robot joint values
                6 angles (deg)

        return: 
            coords
                position (mm), rotation (deg)
                    list [x,y,z,Rx,Ry,Rz]
    
    """

    theta_values = {theta1: sp.rad(t1),  
                    theta2: sp.rad(t2),  
                    theta3: sp.rad(t3),
                    theta4: sp.rad(t4),
                    theta5: sp.rad(t5),
                    theta6: sp.rad(t6)}
  
    #Use T06_nu
    T06_numeric = T06.subs(theta_values).evalf()

    #Extract position values from T06 matrix

    x_pos = round(T06_numeric[0,3],2)
    y_pos = round(T06_numeric[1,3],2)
    z_pos = round(T06_numeric[2,3],2)

    #Calculate rotations in radians

    Rx_rad = math.atan2(T06_numeric[2,1], T06_numeric[2,2])
    Ry_rad = math.atan2(-T06_numeric[2,0], (T06_numeric[2,1]**2+T06_numeric[2,2]**2)**0.5)
    Rz_rad = math.atan2(T06_numeric[1,0], T06_numeric[0,0])

    #Convert to degrees
    #Rounded to 2 decimals

    Rx_deg = round(math.degrees(Rx_rad),2)
    Ry_deg = round(math.degrees(Ry_rad),2)
    Rz_deg = round(math.degrees(Rz_rad),2)

    return (x_pos, y_pos, z_pos, Rx_deg, Ry_deg, Rz_deg)
