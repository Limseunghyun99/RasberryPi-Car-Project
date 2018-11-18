
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
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        self.car.steering.turning_max = 50
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(80)
        print("start")
        while(True):
            print("tracking: ", self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            print("distance: ", distance)
            if 0 < distance <= 30:
                self.car.accelerator.stop()
                self.car.steering.turn(43)
                self.car.accelerator.go_forward(40)
                time.sleep(0.5)
                    while self.car.line_detector.read_digital() != [1,0,0,0,0]:
                        self.car.accelerator.go_forward(60)
                    self.car.steering.turn(120)
                    self.car.accelerator.go_forward(50)
                    time.sleep(1.5)
                    while self.car.line_detector.read_digital()[4] == 0:
                        self.car.accelerator.go_forward(60)
                    
                
            if(self.car.line_detector.read_digital() == [0,0,1,0,0]):
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [1,1,1,1,0]):
                self.car.steering.turn_left(50)
                self.car.accelerator.go_forward(50)

            elif(self.car.line_detector.read_digital() == [1,0,0,0,0] ):
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [1,1,0,0,0]):
                self.car.steering.turn_left(65)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,1,0,0,0]):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,1,1,0,0]):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [1,1,1,0,0]):
                self.car.steering.turn_left(75)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,0,1,1,0]):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,0,1,1,1]):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,0,0,1,0]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,0,0,1,1]):
                self.car.steering.turn_right(105)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [0,0,0,0,1]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(40)
                time.sleep(0.1)

            elif(self.car.line_detector.read_digital() == [0,1,1,1,0]):
                self.car.steering.turn(90)
                self.car.accelerator.go_forward(40)

            elif(self.car.line_detector.read_digital() == [1,0,0,1,1]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(60)

            elif(self.car.line_detector.read_digital() == [1,0,1,1,1]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(50)

            elif(self.car.line_detector.read_digital() == [0,0,0,0,0]):
                self.car.steering.turn_right(120)
                self.car.accelerator.go_backward(40)
                time.sleep(0.33)
                self.car.steering.turn(80)
                self.car.accelerator.stop()

            elif(self.car.line_detector.read_digital() == [1,1,1,1,1]):
                self.car.accelerator.stop()
                break
            else:
                continue
            time.sleep(0.1)
        #self.car.accelerator.stop()
                
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking() 
