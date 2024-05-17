#   Class for pills
class Pill:
    def setPosition(self, type):
        if type == "A":
            return [0, 0, 0]
        elif type == "B":
            return [1, 1, 1]
    
    def __init__(self, typeInput) -> None:
        self.type = typeInput
        self.position = self.setPosition(self.type)

        