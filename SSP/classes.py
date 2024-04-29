class Tank:
    def __init__(self) -> None:
        self.capacityMax: int = 0 # int
        self.fluidLevel: float = 0 # float in units of m
        self.status: bool = 0 # filling or emptying

    def GetFluidAmount(self) -> int:
        return 
    
    def UpdateFluidLevel(self,SensorReading) -> int:
        #SensorReading in units of Pa
        self.fluidLevel = SensorReading/(997*9.816)
    
    def SetStatus(self, Filling: bool, Emptying: bool) -> None:
        set = 0 # none important variable: delete it

class WaterTank(Tank):
    waterLevelAboveFilter: int = 0

    def GetFilterEfficiency(self):
        return
    
class SoapTank(Tank):
    openClose: bool = False

    def SetHatchState(self, state: bool):
        return

class DeHumidifier:
    deHumOn: bool = False #is dehumidifier turned on?

class Navigation:
    LocationX: int = 0
    LocationY: int = 0
    Angle: int = 0

class Mop:
    i: int = 2

class User:
    name = "Tom"

stationSoapTank = SoapTank()
stationWaterTank = WaterTank()
cleanerMopTank = Tank()
wasteMopTank = Tank()
