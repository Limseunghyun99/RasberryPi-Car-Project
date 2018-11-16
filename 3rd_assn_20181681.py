#########################################################################
# Date: 2018/08/09
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################


# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
# import ALL method in the SEN040134 Tracking Module
# =======================================================================
from SEN040134 import SEN040134_Tracking as Tracking_Sensor

# =======================================================================
# import ALL method in the TCS34725 RGB Module
# =======================================================================
from TCS34725 import TCS34725_RGB as RGB_Sensor

# =======================================================================
# import ALL method in the SR02 Ultrasonic Module
# =======================================================================
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor

# =======================================================================
# import ALL method in the rear/front Motor Module
# =======================================================================
import rear_wheels
import front_wheels

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)


class Car(object):

    def __init__(self):
        self.moduleInitialize()

    def drive_parking(self):
        # front wheels center allignment
        self.front_steering.turn_straight()

        # power down both wheels
        self.rear_wheels_drive.stop()
        self.rear_wheels_drive.power_down()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def assignment_main(self):
        # Implement the assignment code here.
        # Example Of Real Motor Control

        distance = 0
        count = 0

        self.distance_detector.ready()
        self.rear_wheels_drive.go_forward(50)
        while (self.line_detector.read_digital() != [0,0,0,0,0]):
            for i in range(0,3):
                count += self.distance_detector.get_distance()
            distance = count/3
            count = 0
            if distance <= 30:
                self.front_steering.turn_left(30)
                if self.line_detector.is_in_line():
                    self.front_steering.turn_right(30)
                    time.sleep(1)
                while (self.line_detector.is_in_line()):
                    if self.line_detector.is_center() == True:
                        if self.line_detector.read_digital()[1] == 1:
                            self.front_steering.turn_left(10)
                        if self.line_detector.read_digital()[3] == 1:
                            self.front_steering.turn_right(10)
                    elif self.line_detector.read_digital()[0] == 1:
                        self.rear_wheels_drive.leftLarge()
                    elif self.line_detector.read_digital()[4] == 1:
                        self.front_steering.turn_right(30)
        self.rear_wheels.drvie.stop()

    def moduleInitialize(self):
        try:
            # ================================================================
            # ULTRASONIC MODULE DRIVER INITIALIZE
            # ================================================================
            self.distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)

            # ================================================================
            # TRACKING MODULE DRIVER INITIALIZE
            # ================================================================
            self.line_detector = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])

            # ================================================================
            # RGB MODULE DRIVER INITIALIZE
            # ================================================================
            self.color_getter = RGB_Sensor.TCS34725()

            # ================================================================
            # FRONT WHEEL DRIVER SETUP
            # ================================================================
            self.front_steering = front_wheels.Front_Wheels(db='config')
            self.front_steering.ready()

            # ================================================================
            # REAR WHEEL DRIVER SETUP
            # ================================================================
            self.rear_wheels_drive = rear_wheels.Rear_Wheels(db='config')
            self.rear_wheels_drive.ready()

            # ================================================================
            # SET LIMIT OF TURNING DEGREE
            # ===============================================================
            self.front_steering.turning_max = 35

            # ================================================================
            # SET FRONT WHEEL CENTOR ALLIGNMENT
            # ================================================================
            self.front_steering.turn_straight()

            # ================================================================
            # DISABLE RGB MODULE INTERRUPTION
            # ================================================================
            self.color_getter.set_interrupt(False)

        except:
            print("MODULE INITIALIZE ERROR")
            print("CONTACT TO Kookmin Univ. Teaching Assistant")


if __name__ == "__main__":
    try:
        car = Car()
        car.assignment_main()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        car.drive_parking()
