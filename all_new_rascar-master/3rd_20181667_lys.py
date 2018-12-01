#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
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
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)
        Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])

        steering = front_wheels.Front_Wheels(db='config')
        steering.center_alignment()

        accelerator = rear_wheels.Rear_Wheels(db='config')

        current = 0
        previous = 0

        line_case = [[1,0,0,0,0], [1,1,0,0,0], [0,1,0,0,0], [0,1,1,0,0], [0,0,1,0,0,],
                     [0,0,1,1,0], [0,0,0,1,0], [0,0,0,1,1], [0,0,0,0,1]]

        line_angle = [-35, -25, -15, -5, 0, 5, 15, 25, 35]

        obstacle = 0

        accelerator.ready()
        accelerator.go_forward(60)

        while True:
            distance = distance_detector.get_distance()
            current = distance
            current, previous == previous, current
            print("Distance : ", distance)
            time.sleep(0.0001)

            if current < (previous - 30) or current > (previous + 30):
                current == previous

                if current <= 40:
                    steering.turn_left(90 + lineAngle[0])
                    if Tracker.read_digital == lineValue[0]:
                        steering.turn_right(90 + lineAngle[8])

            for i in range(len(lineValue)):
                if Tracker.read_digital() == lineValue[i]:
                    steering.turn_left(90 + lineAngle[i])
                    print("turn : {}" .format(lineAngle[i]))
                    time.sleep(0.0001)


            if Tracker.read_digital() == [1, 1, 1, 1, 1]:
                break

        if Tracker.read_digital() == [1, 1, 1, 1, 1]:
            accelerator.stop()
            steering.center_alignment()
            print("rascar stop")

            accelerator.power_down()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
