import math
from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD
import time
mc = MyCobot("COM5", 115200)

def round_up(n, decimals=0):
    multiplier = 10**decimals
    return math.ceil(n * multiplier) / multiplier

def printGetCoords():
    listCords = mc.get_coords()
    x = round_up(listCords[0], 2)
    y = listCords[1]
    z = listCords[2]

    newList = []
    newList.append(x)
    newList.append(y)
    newList.append(z)
    newList.append(listCords[3])
    newList.append(listCords[4])
    newList.append(listCords[5])

    print(newList)

        

mc.set_world_reference([0,0,0,0,0,0])


mc.sync_send_angles([0,0,0,0,0,0],25)
time.sleep(2)

#mc.sync_send_angles([0,-21.8,-115,48,90,0],25)
"""time.sleep(2)
mc.sync_send_coords([100,-250,150,180,0,-180],25,0,timeout=3)
#print("Position 1 = " + str(mc.get_coords()))
printGetCoords()"""

for i in range(1, 11):
    mc.sync_send_coords([100,-250,130,180,0,-180],25,0,timeout=3)
    time.sleep(2)
    print("Position 1 = " + str(mc.get_coords()))
    
    mc.sync_send_coords([-250,20,100,180,0,-180],25,0,timeout=3)
    time.sleep(2)
    print("Position 2 = " + str(mc.get_coords()))

