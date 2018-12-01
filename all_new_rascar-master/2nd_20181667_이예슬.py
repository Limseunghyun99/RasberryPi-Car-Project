#########################################################################
# Date: 2018/10/02
# file name: 2nd_20181667_이예슬.py
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
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
        
        steering = front_wheels.Front_Wheels(db = 'config')
        steering.center_alignment()

        accelerator = rear_wheels.Rear_Wheels(db = 'config')
        accelerator.ready()
        accelerator.go_forward(80)
        
        while Tracker.is_in_line() != False:
            print("line detected")
            time.sleep(0.0001)
            
            if Tracker.read_digital()[1] == 1:
                steering.turn_left(80)
                print("turn left : 10")
                time.sleep(0.0001)
                
            elif Tracker.read_digital()[3] == 1:
                steering.turn_right(100)
                print("turn right : 10")
                time.sleep(0.0001)
                
            elif Tracker.read_digital()[0] == 1:
                steering.turn_left(60)
                print("turn left : 30")
                time.sleep(0.0001)
                
            elif Tracker.read_digital()[4] == 1:
                steering.turn_right(120)
                print("turn right : 30")
                time.sleep(0.0001)
            
            if Tracker.read_digital() == [0,0,0,0,0]:
                break
                    
        if Tracker.is_in_line() == False:
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
