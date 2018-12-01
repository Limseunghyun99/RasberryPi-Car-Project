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


        current_line = Tracker.read_digital()

        line_case = [[1,0,0,0,0], [1,1,0,0,0], [0,1,0,0,0], [0,1,1,0,0], [0,0,1,0,0], [0,0,1,1,0], [0,0,0,1,0], [0,0,0,1,1], [0,0,0,0,1]]

        line_angle = [-35, -25, -15, -5, 0, 5, 15, 25, 35]
        
        previous_line = [0,0,0,0,0]

        obstacle = 0
        count = 0
        
        accelerator.ready()
        accelerator.go_forward(60)

        while True:
            print(current_line)
            time.sleep(0.0001)
            distance = distance_detector.get_distance()
            print("Distance : ", distance)
            time.sleep(0.0001)

            if 0 < distance <= 35 and distance != -1:
                count += 1
            
            if count >= 10:
                accelerator.stop()
                steering.turn(90 + line_angle[0])
                accelerator.go_forward(60)
                time.sleep(1)
                accelerator.stop()
                time.sleep(0.01)
                steering.turn(90 + line_angle[8])
                accelerator.go_forward(60)
                time.sleep(1.9)
                obstacle += 1
                print("count obstacle : ", obstacle)
                obstacle = 0
                while True:
                    if current_line != [0,0,0,0,0]:
                        break
            
            if current_line == line_case[0]:
                steering.turn(90 + line_angle[0])
                accelerator.go_forward(60)
            
            elif current_line == line_case[1]:
                steering.turn(90 + line_angle[1])
                accelerator.go_forward(60)
            
            elif current_line == line_case[2]:
                steering.turn(90 + line_angle[2])
                accelerator.go_forward(60)
            
            elif current_line == line_case[3]:
                steering.turn(90 + line_angle[3])
                accelerator.go_forward(60)
            
            elif current_line == line_case[4]:
                steering.turn(90 + line_angle[4])
                accelerator.go_forward(60)
            
            elif current_line == line_case[5]:
                steering.turn(90 + line_angle[5])
                accelerator.go_forward(60)
            
            elif current_line == line_case[6]:
                steering.turn(90 + line_angle[6])
                accelerator.go_forward(60)
            
            elif current_line == line_case[7]:
                steering.turn(90 + line_angle[7])
                accelerator.go_forward(60)
                
            elif current_line == line_case[8]:
                steering.turn(90 + line_angle[8])
                accelerator.go_forward(60)
            
            if current_line == [0,0,0,0,0]:
                steering.turn_right(100)
                accelerator.go_backward(60)
                time.sleep(0.33)
                accelerator.stop()
                
            elif current_line == [1,1,1,1,1]:
                if obstacle == 2:
                    accelerator.stop()
                    break
                else:
                    continue


        #accelerator.stop()
        #steering.center_alignment()
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
