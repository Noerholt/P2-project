from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations

import program
 
# Any interaction with RoboDK must be done through
# Robolink()
RL = Robolink()
 
# get the robot item:
robot = RL.Item('MyCoBot_320')
 
# get the home target and the welding targets:
home = RL.Item('home')
pillA = RL.Item('pill A')
pillAapp = RL.Item('pill A app')
pillB = RL.Item('pill B')
pillBapp = RL.Item('pill B app')
# get the pose of the target (4x4 matrix):

#program.runProgram([["B","A"],["A","A","B"]])

# move the robot to home, then to the center:
robot.MoveJ(home)
robot.MoveJ(pillAapp)
robot.MoveL([-48.946770, -65.509573, -96.859159, 72.368732, 90.000000, 41.053230])

robot.MoveL(pillAapp)
x = 1

if x == 1:
    robot.MoveJ(home)
    robot.MoveJ(pillBapp)
    robot.MoveL(pillB)
    robot.MoveL(pillAapp)
    print("Final destination!")
