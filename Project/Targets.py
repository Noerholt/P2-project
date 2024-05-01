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

home = targets([0,0,0,0,0,0])

class pillDivider(targets):
    def __init__(self,coords,timeOfDay):
        super().__init__(coords)

        self.timeOfDay = timeOfDay

pillDividerMorning = pillDivider([1,1,1,1,1,1],"morning")

print(pillDividerMorning.timeOfDay)