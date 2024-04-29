stationSoapTank = SoapTank()
stationWaterTank = Water_Tank()
sleanerMopTank = Tank()
sasteMopTank = Tank()


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
        
        
        
