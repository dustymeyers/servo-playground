# import libraries
import RPi.GPIO as GPIO
import time

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # note 11 is pin, 50 = 50Hz pulse

# start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print("Waiting for 2 seconds")
time.sleep(2)

# move the servo
print("Rotating 180 degrees in 10 steps")


# define duty variable
duty = 2

# loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    

# Wait a couple of seconds
time.sleep(2)

# Turn back to 90 degrees
print("turning back to 90 degrees for 2 seconds")
servo1.ChangeDutyCycle(7)
time.sleep(2)

print("Turning back to 0 degrees")
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)

# Clean things up
servo1.stop()
GPIO.cleanup()
print("Completed...")