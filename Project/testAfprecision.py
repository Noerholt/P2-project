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
mc.sync_send_angles([0,0,0,0,0,0,],25)
for i in range(1, 11): 
    mc.sync_send_angles([0,0,0,0,0,0,],25)
    time.sleep(2)
    mc.sync_send_coords([100,-250,200,180,0,180],25,0,1)
    time.sleep(2)
    mc.sync_send_coords([100,-250,176,180,0,180],25,1,2)
    print(f"Position {i} = " + str(mc.get_coords()))

mc.sync_send_angles([0,0,0,0,0,0,],25)