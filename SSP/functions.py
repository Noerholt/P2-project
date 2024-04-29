StationSoapTank = SoapTank()
StationWaterTank = Water_Tank()
CleanerMopTank = Tank()
WasteMopTank = Tank()


humidity=80 #relativ luftfugtighed fra 0-100%
deHumOn=False #status for if dehumidifier is turned on
filterRate=20 #the rate which the filter lets water through

def deHumControl(humidity, StationWaterTank.GetFluidAmount()):
    if humidity<30 or StationWaterTank.FluidLevel>=80:
        deHumOn=False
    else:
        deHumOn=True

def waterTankControl(GetFluidAmount(StationWaterTank)):
    if StationWaterTank.FluidLevel>=95:
        wInputClose()
        
        
        
        
