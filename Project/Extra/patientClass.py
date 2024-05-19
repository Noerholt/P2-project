#   Class for patients
class Patient:
    def appendDayLists(self, morning: list, noon: list, evening: list, night: list) -> None:
        self.fullList.append(morning)
        self.fullList.append(noon)
        self.fullList.append(evening)
        self.fullList.append(night)


    def __init__(self, nameIn, morningIn: list, noonIn: list, eveningIn: list, nightIn: list) -> None:
        self.name = nameIn
        self.morningPillList = morningIn
        self.noonPillList = noonIn
        self.eveningPillList = eveningIn
        self.nightPillList = nightIn

        self.fullList = []
        self.appendDayLists(self.morningPillList, self.noonPillList, self.eveningPillList, self.nightPillList)

