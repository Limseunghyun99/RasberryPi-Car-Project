#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


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
        distance = 0
        count = 0

        self.car.accelerator.go_forward(50)
        while self.car.line_detector.read_digital() != [1,1,1,1,1]:
            if self.car.line_detector.is_center() == True:
                if self.car.line_detector.read_digital()[1] == 1:
                    self.car.steering.turn_left(10)
                if self.car.line_detector.read_digital()[3] == 1:
                    self.car.steering.turn_right(10)
                else:
                    self.car.steering.center_alignment()
            elif self.car.line_detector.read_digital()[0] == 1:
                self.car.accelerator.leftLarge()
                if self.car.line_detector.is_center == True:
                    self.car.steering.center_alignment()
            elif self.car.line_detector.read_digital()[4] == 1:
                self.car.steering.turn_right(30)
            elif self.car.line_detector.read_digital() == [0,0,0,0,0]:
                self.car.accelerator.go_backward(50)

            for i in range(0,3):
                count += self.car.distance_detector.get_distance()
            distance = count/3
            count = 0

            if distance < 30:
                self.car.steering.turn_left(30)
                if self.car.line_detector.is_in_line():
                    self.car.steering.turn_right(30)


            if self.car.distance_detector.get_distance()
            if self.car.line_detector.read_digital() == [1,1,1,1,1]:
                self.car.accelerator.stop()

        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()