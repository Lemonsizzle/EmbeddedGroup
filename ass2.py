from sense_emu import SenseHat
import RPi.GPIO as GPIO
import time

# Initialize the Sense HAT
sense = SenseHat()

# Initialize GPIO for servo motor
GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
pwm.start(0)  # Initial duty cycle of 0%

class gimbal:


def set_servo_angle(angle):
    duty_cycle = (angle / 180.0) * 10 + 2.5
    pwm.ChangeDutyCycle(duty_cycle)

try:
    while True:
        # Read pitch from Sense HAT
        orientation = sense.get_orientation()
        
        for key in orientation:
            print(key, orientation[key])

        print()


        pitch = orientation['pitch']

        # Code for clamping pitch

        # Code for creating a new home orientation

        # Map pitch to servo angle (Assuming 0-180 degrees)
        servo_angle = pitch  # Modify this as needed

        # print(servo_angle)

        # Update servo position
        set_servo_angle(servo_angle)

        time.sleep(0.1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

