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

        avoidance = 0  # 각 동작들의 진행 상황을 알리는 지표
        obstacle = 0 # 장애물 35cm 이내로 감지 시 감지했음을 알림
        goBack = 0 # 코너 도는 중 라인트래커 센서가 라인 이탈 시 후진하도록 지정
        count = 0 # 지금까지 돈 바퀴 수
        angle = 0
        
        current = 0
        previous = 0
        
        accelerator.ready()
        accelerator.go_forward(60)

        while True:
            if goBack == 1:# 커브 회전 중 라인트래커 이탈한 경우에 필요
                goBack = 0
                accelerator.stop()
                steering.turn(90 + line_angle[0])
                accelerator.go_forward(60)

            if avoidance == 0:
                distance = distance_detector.get_distance() # 초음파 센서의 값이 튀는 것에 대한 에러처리
                current = distance
                current, previous == previous, current

                print("Distance : ", distance)
                time.sleep(0.0001)


                if current < (previous - 30) or current > (previous + 30): # 초음파 센서의 값이 튀는 것에 대한 에러처리
                    current == previous

                    if 0 < current <= 35:
                        obstacle = 1
                        print("Obstacle detected")
                    else:
                        pass

            if obstacle == 0: # 라인 주행에 필요

                for i in range(len(line_case)):
                    if current_line == line_case[i]:
                        steering.turn(90 + line_angle[i])
                        previous_line = current_line

                        if avoidance == 1:
                            avoidance = 2
                            print("avoidance 1 -> 2")
                        elif avoidance == 3:
                            avoidance = 0
                            print("avoidance 3 -> 0")

                        break

            elif obstacle == 1: # 장애물 회피에 필요
                print("obstacle 1")
                steering.turn(90 + line_angle[2])
                print("turn")
                avoidance = 1
                obstacle = 0

                while True:
                    if current_line == [0,0,0,0,0]:
                        print("Exit main track")
                        break
                    else:
                        pass

                while True:
                    if Tracker.is_in_line() == True:
                        print("Line detected")
                        break
                    else:
                        pass
        elif avoidance == 1:
            pass

        elif avoidance == 2:
            avoidance = 3
            print("avoidance 2 -> 3")
            steering.turn(90 + line_angle[6])

        elif avoidance == 3:
            pass


            if current_line == [0,0,0,0,0]: # 급커브 회전에 필요

                if obstacle == 0 and avoidance == 0:

                    if previous_line[4] == 1 or previous_line[3] == 1:
                        angle = 90 + line_angle[0]
                    elif previous_line[0] == 1 or previous_line[1] == 1:
                        angle = 90 + line_angle[8]
                    else:
                        pass

                    accelerator.stop()
                    steering.turn(angle)
                    accelerator.go_backward(35)

                    goBack = 1

                    while True: # 라인 중앙 찾은 경우
                        if current_line[2] == 1:
                            break
            elif current_line == [1,1,1,1,1]: # 몇바퀴 돌았는지 세는 데 필요
                count += 1

                if count == 2:
                    accelerator.stop()
                else:
                    while True:
                        if current_line != [1,1,1,1,1]:
                            break
                        

            

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
