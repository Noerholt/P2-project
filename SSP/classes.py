class Tank:
    def __init__(self) -> None:
        
        self.CapacityMax: int = 0 # int
        self.FluidLevel: int = 0 # int
        self.Status: bool = [] # filling and emptying

    def GetFluidAmount(self) -> int:
        return
    
    def UpdateFluidLevel(self) -> int:
        return
    
    def GetStatus(self) -> bool:
        return
    
    def SetStatus(self, Filling: bool, Emptying: bool) -> None:
        set = 0 # none important variable: delete it

class Water_Tank(Tank):
    WaterLevelAboveFilter: int = 0

    def GetFilterEfficiency(self):
        return
    
class SoapTank(Tank):
    open_close: bool = False

    def SetHatchState(self, state: bool):
        return

class DeHymidifier:
    print

class Navigation:
    LocationX: int = 0
    LocationY: int = 0
    Angle: int = 0

class Mop:
    i: int = 2

class User:
    name = "Tom"

StationSoapTank = SoapTank()
StationWaterTank = Water_Tank()
CleanerMopTank = Tank()
WasteMopTank = Tank()


