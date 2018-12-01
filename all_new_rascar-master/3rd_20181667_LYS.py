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

        line_angle = [-40, -35, -25, -15, -5, 0, 5, 15, 25, 35, 40]

        count = 0
        lab = 0

        accelerator.ready()
        accelerator.go_forward(60)
        print("rascar go")

        while True:
            current_line = Tracker.read_digital()
            distance = distance_detector.get_distance()

            print(current_line)
            print(distance)

            if distance <= 35 and distance != -1:
                count += 1
            
            if count >= 10:
                accelerator.stop()
                time.sleep(0.001)
                steering.turn(90 + line_angle[0])
                accelerator.go_forward(60)
                time.sleep(1.8)
                
                steering.turn(90 + line_angle[10])
                accelerator.go_forward(60)
                time.sleep(2.8)
                lab += 1
                print("lab : ", lab)
                count = 0
                while True:
                    if current_line != [0,0,0,0,0]:
                        break


            if current_line == [0,0,1,0,0]:
                accelerator.go_forward(60)

            elif current_line == [1,0,0,0,0]:
                steering.turn(90 + line_angle[0])
                accelerator.go_forward(60)

            elif current_line == [1,1,0,0,0]:
                steering.turn(90 + line_angle[1])
                accelerator.go_forward(60)

            elif current_line == [0,1,0,0,0]:
                steering.turn(90 + line_angle[2])
                accelerator.go_forward(60)

            elif current_line == [0,1,1,0,0]:
                steering.turn(90 + line_angle[3])
                accelerator.go_forward(60)

            elif current_line == [1,1,1,0,0]:
                steering.turn(90 + line_angle[4])
                accelerator.go_forward(60)

            elif current_line == [0,0,1,1,0]:
                steering.turn(90 + line_angle[6])
                accelerator.go_forward(60)

            elif current_line == [0,0,1,1,1]:
                steering.turn(90 + line_angle[7])
                accelerator.go_forward(60)

            elif current_line == [0,0,0,1,0]:
                steering.turn(90 + line_angle[8])
                accelerator.go_forward(60)

            elif current_line == [0,0,0,1,1]:
                steering.turn(90 + line_angle[9])
                accelerator.go_forward(60)

            elif current_line == [0,0,0,0,1]:
                steering.turn(90 + line_angle[10])
                accelerator.go_forward(60)

            elif current_line == [0,0,0,0,0]:
                steering.turn(90 + line_angle[7])
                accelerator.go_backward(60)
                time.sleep(0.35)
                accelerator.stop()

            elif current_line == [1,1,1,1,1]:
                if lab == 2:
                    accelerator.stop()
                    break

            else:
                continue
        

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