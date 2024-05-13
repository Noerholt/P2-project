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

######################################################

#pill container targets

containerApproachPillA = targets([1,1,30,1,1,1])

containerPillA = targets([1,1,1,1,1,1])

containerApproachPillB = targets([2,2,30,2,2,2])

containerPillB = targets([1,1,1,1,1,1])

######################################################

#pill divider box targets

pillDividerMorningApproach = targets([1,1,30,1,1,1])

pillDividerMorning = targets([1,1,1,1,1,1])

pillDividerAfternoonApproach = targets([1,1,30,1,1,1])

pillDividerAfternoon = targets([2,2,2,2,2,2])

pillDividerEveningApproach = targets([1,1,30,1,1,1])

pillDividerEvening = targets([3,3,3,3,3,3])

######################################################