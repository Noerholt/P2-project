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

    def update_coords(self, new_coords):
        self.coords = new_coords

    def update_single_coord(self, index, value):
        self.coords[index] = value

######################################################

#home position
home = targets([0,0,0,0,0,0])

#viapoint position
viapoint = targets([-195,-225,130,180,0,0])

######################################################

#pill container targets
                        
ApproachPillA = targets([-50,-210,50,-180,0,0])

PickPillA = targets([-55,-215,41,-180,0,0])

ApproachPillB = targets([55,-210,50,-180,0,0])

PickPillB = targets([55,-215,37,-180,0,90])

######################################################

#pill divider box targets

MorningApproach = targets([-260,-100,60,-180,0,0])

MorningDrop = targets([-260,-15,70,-180,0,0])

AfternoonApproach = targets([-260,-60,60,-180,0,0])

AfternoonDrop = targets([-260,-45,70,-180,0,0])

EveningApproach = targets([-260,-20,60,-180,0,0])

EveningDrop = targets([-260,-15,70,-180,0,0])

NightApproach = targets([-260,20,60,-180,0,0])

NightDrop = targets([-260,15,70,-180,0,0])

#####################################################

#lists of targets

#dayContainer targets:

dayTargetsApproach = [MorningApproach, AfternoonApproach, EveningApproach, NightApproach]
dayTargetsDrop = [MorningDrop, AfternoonDrop, EveningDrop, NightDrop]