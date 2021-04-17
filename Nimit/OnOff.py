# Written by Nimit
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) #GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)


for i in range(10): 
    GPIO.output(12,i%2)
    time.sleep(1)
    print(i)
