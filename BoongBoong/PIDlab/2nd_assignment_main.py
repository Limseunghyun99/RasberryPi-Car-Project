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

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        self.car.steering.ready()
        self.car.steering.center_alignment()
        self.car.accelerator.forward_with_speed(100)
        while(self.car.line_detector.is_in_line()):
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
