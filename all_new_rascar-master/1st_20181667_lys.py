#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################
import RPi.GPIO as GPIO
import time

from SEN040134 import SEN040134_Tracking as Tracking_Sensor

from SR02 import SR02_Supersonic as Supersonic_Sensor

import rear_wheels
import front_wheels

from car import Car



class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

        steering = front_wheels.Front_Wheels(db = 'config')
        steering.center_alignment()

        accelerator = rear_wheels.Rear_Wheels(db = 'config')
        accelerator.ready()

        current = 0
        previous = 0

        start_time = time.time()

        accelerator.go_forward(100)

        while True:
            distance = distance_detector.get_distance()
            current = distance
            current, previous == previous, current
            print("Distance : ", distance)
            time.sleep(0.0001)

            if current < (previous - 25) or current > (previous + 25):
                current == previous

            if 40 < current <= 60:
                accelerator.go_forward(95)

            elif 20 < current <= 40:
                accelerator.go_forward(90)

            elif 0 < current <= 10:
                accelerator.stop()
                steering.center_alignment()
                time.sleep(0.1)
                stop_time = time.time()
                time.sleep(0.01)
                break
            else:
               continue

        accelerator.go_backward(75)
        time.sleep(stop_time-start_time)

        accelerator.stop()
        accelerator.power_down()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
