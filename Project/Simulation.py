from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations

import program
 
# Any interaction with RoboDK must be done through
# Robolink()
RL = Robolink()
 
# get the robot item:
robot = RL.Item('MyCoBot_320')
 
# get the home target and the welding targets:
home = RL.Item('Target 1')
target = RL.Item('Target 2')
# get the pose of the target (4x4 matrix):
poseref = target.Pose()

program.runProgram([["B","A"],["A","A","B"]])

# move the robot to home, then to the center:
robot.MoveJ(home)
robot.MoveJ(target)
x = 1

if x == 1:
    robot.MoveJ(home)
    robot.MoveJ(target)
    print("Final destination!")
