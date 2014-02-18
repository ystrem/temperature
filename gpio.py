from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) #Green LED

GPIO.output(17,True)
sleep(2)
GPIO.output(17,False)

GPIO.cleanup(17)
