import os
import time
from Product.kinematicsLibrary import *
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

os.system('cls')
mc = MyCobot("COM1", 115200)
mc.sync_send_angles([0,0,0,0,0,0],30)

T = TransformDesired(-55,-215,130,-180,0,0)
S = CalculateThetaValues(T)
PrintAngleSolution(S)
anglesDesired = []

for i in range(6):
    anglesDesired.append(ToDeg(S[0,i]))

print("Running")
mc.sync_send_angles(anglesDesired,30)
print("Adjusting")
AdjustAngles(mc,anglesDesired)