#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.kp = 10
        self.ki = 0
        self.kd = 0
        self.pre_error = 0
        self.errorsum = 0

    def errorvalue(self):
        if self.car.line_detector.read_digital() == [1,0,0,0,0]:
            return (30,-10)
        elif self.car.line_detector.read_digital() == [1,1,0,0,0]:
            return -7.5
        elif self.car.line_detector.read_digital() == [0,1,0,0,0]:
            return -5
        elif self.car.line_detector.read_digital() == [0,1,1,0,0]:
            return -2.5
        elif self.car.line_detector.read_digital() == [0,0,1,0,0]:
            return 0
        elif self.car.line_detector.read_digital() == [0,0,1,1,0]:
            return 2.5
        elif self.car.line_detector.read_digital() == [0,0,0,1,0]:
            return 5
        elif self.car.line_detector.read_digital() == [0,0,0,1,1]:
            return 7.5
        elif self.car.line_detector.read_digital() == [0,0,0,0,1]:
            return 10

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        self.car.accelerator.forward_with_speed(100)

        while(self.car.line_detector.is_in_line()):
            error = self.errorvalue()
            self.errorsum += error
            pre_error = error

            p = kp * error
            #i = ki * count
            #d = kd * (error-pre_error)
            #value = p+i+d


            if self.car.line_detector.is_center() == True:
                if self.car.line_detector.read_digital()[1] == 1:
                    self.car.steering.turn_left(10)
                if self.car.line_detector.read_digital()[3] == 1:
                    self.car.steering.turn_right(10)
            elif self.car.line_detector.read_digital()[0] == 1:
                self.car.steering.turn_left(30)
            elif self.car.line_detector.read_digital()[4] == 1:
                self.car.steering.turn_right(30)
        self.car.accelerator.stop()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
