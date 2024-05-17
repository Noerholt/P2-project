from pillClass import Pill

pillA = Pill("A")
pillB = Pill("B")

class ListCreator:
    def createList(self, listIn: list) -> None:
        for list in listIn:
            for pill in list:
                if pill == "A":
                    self.pillPosList.append(pillA.position)
                elif pill == "B":
                    self.pillPosList.append(pillB.position)

    def __init__(self, listIn: list) -> None:
        self.pillPosList = []
        self.createList(listIn)



