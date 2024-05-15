#All targets should be defined in this file
#Define targets with position and orientation as seperate lists, as described in class description.
#Check existing targets to avoid duplicates


class targets:

    """Define targets

        properties:
            position and orientation (mm, deg)
                list [x,y,z,Rx,Ry,Rz]
            
    """

    def __init__(self,coords):

        self.coords = coords

######################################################

#home position
home = targets([0,0,0,0,0,0])

#viapoint position
viapoint = targets([-195,-225,130,180,0,0])

######################################################

#pill container targets

ApproachPillA = targets([-50,-250,130,-180,0,0])

PickPillA = targets([-50,-250,60,-180,0,0])

ApproachPillB = targets([50,-250,130,-180,0,0])

PickPillB = targets([50,-250,60,-180,0,0])

######################################################

#pill divider box targets

MorningApproach = targets([-250,-75,130,-180,0,0])

MorningDrop = targets([-250,-75,70,-180,0,0])

AfternoonApproach = targets([-250,-45,130,-180,0,0])

AfternoonDrop = targets([-250,-45,70,-180,0,0])

EveningApproach = targets([-250,-15,130,-180,0,0])

EveningDrop = targets([-250,-15,70,-180,0,0])

NightApproach = targets([-250,15,130,-180,0,0])

NightDrop = targets([-250,15,70,-180,0,0])

#####################################################

#lists of targets

#dayContainer targets:

dayTargetsApproach = [MorningApproach, AfternoonApproach, EveningApproach, NightApproach]
dayTargetsDrop = [MorningDrop, AfternoonDrop, EveningDrop, NightDrop]