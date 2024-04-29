import classes

stationSoapTank = classes.SoapTank()
stationWaterTank = classes.WaterTank()
sleanerMopTank = classes.Tank()
sasteMopTank = classes.Tank()

dehumidifier=classe.DeHumidifier()

humidity=80 #relativ luftfugtighed fra 0-100%
filterRate=20 #the rate which the filter lets water through

def deHumControl(humidity):
    if humidity<30 or stationWaterTank.FluidLevel>=80:
        deHumOn.dehumidifier=False
    else:
        deHumOn.dehumidifier=True

def waterTankControl():
    
    if stationWaterTank.FluidLevel>=95:
        wInputClose()
        
        
        
