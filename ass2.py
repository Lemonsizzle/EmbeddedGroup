from sense_emu import SenseHat
import RPi.GPIO as GPIO
import time
from ass2_db import db

# Initialize the Sense HAT
sense = SenseHat()

# Initialize GPIO for servo motor
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
pwm.start(0)  # Initial duty cycle of 0%

db = db()

offset = 0
rotate_delta = 5


def set_servo_angle(angle):
    duty_cycle = (angle / 180.0) * 10 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:

        timestamp = datetime.now()

        temperature = sense.get_temperature()
        humidity = sense.get_humidity()

        orientation = sense.get_orientation()

        roll = orientation['roll']
        pitch = orientation['pitch']
        yaw = orientation['yaw']


        # Read pitch from Sense HAT
        orientation = sense.get_orientation()
        
        for key in orientation:
            print(key, orientation[key])

        pitch = orientation['pitch']

        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "middle":
                    # Stick pressed, set servo to 0 deg
                    offset = pitch + offset
                elif event.direction == "left":
                    offset -= rotate_delta
                elif event.direction == "right":
                    offset += rotate_delta
     

        # Code for clamping pitch

        # Map pitch to servo angle (Assuming 0-180 degrees)
        servo_angle = pitch + offset

        # Update servo position
        set_servo_angle(servo_angle)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

