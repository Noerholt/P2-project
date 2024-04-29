import classes

stationSoapTank = classes.SoapTank()
stationWaterTank = classes.WaterTank()
cleanerMopTank = classes.Tank()
wasteMopTank = classes.Tank()

dehumidifier=classe.DeHumidifier()

humidity=80 #relative himidity from 0-100%
filterRate=20 #the rate which the filter lets water through

def deHumControl(humidity):
    if humidity<30 or stationWaterTank.FluidLevel>=80:
        deHumOn.dehumidifier=False
    else:
        deHumOn.dehumidifier=True

def waterTankControl():
    
    if stationWaterTank.FluidLevel>=95:
        wInputClose() #command which closes the water input for the watertank
        
        
