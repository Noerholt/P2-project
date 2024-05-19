import os
import time
from Product.kinematicsLibrary import *
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

os.system('cls')
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

"""
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