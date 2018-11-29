
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time
import threading


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.car.steering.turning_max = 50

    def drive_parking(self):
        self.car.drive_parking()

    def side_parking(self):
        self.adequate_time = 1
        self.car.steering.turn(70)
        self.car.accelerator.go_forward(30)
        time.sleep(0.5)
        self.car.steering.turn(90)
        self.car.accelerator.go_backward(30)
        time.sleep(0.6)
        self.car.accelerator.rightLarge()
        time.sleep(self.adequate_time)
        self.car.accelerator.stop()

    def from_side_to_road(self):
        self.car.accelerator.leftLarge()
        time.sleep(self.adequate_time)
        self.car.steering.turn(120)
        self.car.accelerator.go_forward
        time.sleep(0.5)

    def line_tracing(self):
        if (self.car.line_detector.read_digital() == [0, 0, 1, 0, 0]):
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [1, 1, 1, 1, 0]):
            self.car.steering.turn_left(50)
            self.car.accelerator.go_forward(50)

        elif (self.car.line_detector.read_digital() == [1, 0, 0, 0, 0]):
            self.car.steering.turn_left(45)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [1, 1, 0, 0, 0]):
            self.car.steering.turn_left(50)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 1, 0, 0, 0]):
            self.car.steering.turn_left(55)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 1, 1, 0, 0]):
            self.car.steering.turn_left(60)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [1, 1, 1, 0, 0]):
            self.car.steering.turn_left(70)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 0, 1, 1, 0]):
            self.car.steering.turn_right(95)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 0, 1, 1, 1]):
            self.car.steering.turn_right(95)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 0, 0, 1, 0]):
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 0, 0, 1, 1]):
            self.car.steering.turn_right(105)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [0, 0, 0, 0, 1]):
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(40)
            time.sleep(0.1)

        elif (self.car.line_detector.read_digital() == [0, 1, 1, 1, 0]):
            self.car.steering.turn(90)
            self.car.accelerator.go_forward(40)

        elif (self.car.line_detector.read_digital() == [1, 0, 0, 1, 1]):
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(60)

        elif (self.car.line_detector.read_digital() == [1, 0, 1, 1, 1]):
            self.car.steering.turn_right(110)
            self.car.accelerator.go_forward(50)

        elif (self.car.line_detector.read_digital() == [0, 1, 1, 1, 1]):
            self.car.steering.turn(70)
            self.car.accelerator.go_forward(50)

        elif (self.car.line_detector.read_digital() == [0, 0, 0, 0, 0]):
            self.car.steering.turn(130)
            self.car.accelerator.go_backward(40)
            time.sleep(0.5)
            self.car.steering.turn(80)
            self.car.accelerator.stop()

        elif (self.car.line_detector.read_digital() == [1, 1, 1, 1, 1] and count >= 2):
            self.car.accelerator.stop()

    def avoidence(self):
        distance = self.car.distance_detector.get_distance()



    def car_startup(self):
        a = self.avoidence()
        b = self.line_tracing()
        a.thread
        b.thread

        while(True):
            print("tracking: ", self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            print("distance: ", distance)
            if 0 < distance <= 30:
                count += 1
                
                    

        #self.car.accelerator.stop()
                
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking() 
