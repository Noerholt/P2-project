import classes

stationSoapTank = classes.SoapTank()
stationWaterTank = classes.WaterTank()
sleanerMopTank = classes.Tank()
sasteMopTank = classes.Tank()

humidity=80 #relativ luftfugtighed fra 0-100%
deHumOn=False #status for if dehumidifier is turned on
filterRate=20 #the rate which the filter lets water through

def deHumControl(humidity):
    if humidity<30 or stationWaterTank.FluidLevel>=80:
        deHumOn=False
    else:
        deHumOn=True

def waterTankControl():
    
    if stationWaterTank.FluidLevel>=95:
        wInputClose()
        
        
        
