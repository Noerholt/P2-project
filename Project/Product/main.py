import os
import time
from kinematicsLibrary import *
from Targets import *
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD

os.system('cls')
mc = MyCobot("COM17", 115200)
mc.power_on()
mc.sync_send_angles(home.coords,30)
time.sleep(1)
mc.set_color(255,0,0)
mc.set_color(255,0,0)

List1 =[["A","A","B","B","B","B"],["A","A","A","B"],["B","B","A","B"],["B","A","A","A"]]
List2 =[["A","A","A","A","A","A","A","A","A"],["B","B","B","B","B","B","B","B","B"],[],[]]
List3 =[["A","A","A","A","A"],["B","B","B","B","B"],["A","A","A","A"],["B","B","B","B"]]
List4 =[["A","B"],["A","B"],["A","B"],["A","B"]]
List5 =[["A"],["A"],["A"],["A"]]
List6 =[["A","A","A","B","B",],["A","A","B","B","B"],["B","B","A","A"],["B","B","A","A"]]

targetPositions = {'A': ApproachPillA.coords, 'B': ApproachPillB.coords}
dispenserPositions = [MorningApproach.coords, AfternoonApproach.coords, EveningApproach.coords, NightApproach.coords]

ProcessList(mc, List6, targetPositions, dispenserPositions)
mc.sync_send_angles(home.coords,30)