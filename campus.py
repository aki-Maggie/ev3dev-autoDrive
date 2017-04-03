#this part of code for campass

#Connect campass
gs = GyroSensor()
gs.mode = 'GYRO-ANG'	# Changing the mode resets the gyro
gs.mode = 'GYRO-RATE'	# Set gyro mode to return compass angle

def gyro_reset():
    gs.mode = 'GYRO-ANG'
    gs.mode = 'GYRO-RATE'
	
	
def Gyro_isEnemy():
	gyro_reset()
	if (gs.value() > -10 & gs.value() < 10):
        return 1;
    return 0;
	
