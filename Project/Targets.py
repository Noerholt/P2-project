#All targets should be defined in this file
#Define targets with position and orientation as seperate lists, as described in class description.
#Check existing targets to avoid duplicates


class target:

    """Define targets

        properties:
            position (mm)
                list [x,y,z]

            orientation (deg)
                list [Rx,Ry,Rz]
            
    """

    def __init__(self,position,orientation):

        self.position = position
        self.orientation = orientation

home = target([0,0,0],[0,0,0])
