import os
import time
from kinematicsLibraryCopy import *
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

os.system('cls')

T1 = TransformDesired([150,-100,500,90,45,45])
T2 = TransformDesired([-200,-150,455,100,-40,-15])
T3 = TransformDesired([-350,-88.78,239.4,0,0,90])
T4 = TransformDesired([100,-250,176,-180,0,0])

np.set_printoptions(suppress=True, precision=6)
print(np.round(T4,6))
S = CalculateThetaValues(T4)
PrintAngleSolution(S)

"""
[     0.559882,     0.545801,     0.623405,   145.118163 ;
      0.545801,     0.323140,    -0.773099,  -107.159011 ;
     -0.623405,     0.773099,    -0.116978,   502.367258 ;
      0.000000,     0.000000,     0.000000,     1.000000 ];

mc = MyCobot("COM1", 115200)
mc.power_on()

mc.sync_send_angles([0,0,0,0,0,0],30)
mc.set_color(255,0,0)

mc.sync_send_angles(Solution(mc, [55,-210,50,-180,0,0], "P2"),30)
LinearMotionA(mc, Solution(mc, [52.5,-207.5,-5,-180,0,0], "P2"), 100)
mc.set_color(0,255,0)
mc.set_color(0,255,0)
mc.set_color(0,255,0)
time.sleep(1)
LinearMotionA(mc, Solution(mc, [55,-210,50,-180,0,0], "P2"), 100)

mc.sync_send_angles(Solution(mc, [-260,-15,100,-180,0,0], "P1"),30)
print(ToDeg(CalculateThetaValues(TransformDesired([-260,-15,100,-180,0,0]))))
LinearMotionA(mc, Solution(mc, [-260,-15,20,-180,0,0], "P1"), 100)
mc.set_color(255,0,0)

time.sleep(3)

S = CalculateThetaValues(TransformDesired([-105,-215,50,-180,0,0]))
anglesDesired = ChooseSolution(mc, ToDeg(S), "B")
mc.sync_send_angles(anglesDesired,30)
AdjustAngles(mc, anglesDesired)

S = CalculateThetaValues(TransformDesired([-105,-215,15,-180,0,0]))
anglesDesired = ChooseSolution(mc, ToDeg(S), "B")


print("Running")
mc.sync_send_angles(anglesDesired,30)
print("Adjusting")
start = time.time()
AdjustAngles(mc,anglesDesired)
print(f"{'Time taken:'}{time.time()-start}")
"""