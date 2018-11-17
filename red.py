
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
        distance = self.car.distance_detector.get_distance()
        self.car.accelerator.go_forward(40)
        count = 0
        print("start")
        countstop = 0
        while(True):
            print(self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            print(distance)
            if distance == -1:
                continue
            if distance <= 20:
                count += 1
            if count >= 10:
                self.car.accelerator.stop()
                self.car.steering.turn_left(55)
                self.car.accelerator.go_forward(50)
                time.sleep(1)
                self.car.accelerator.stop()
                self.car.steering.turn_right(165)
                self.car.accelerator.go_forward(80)
                time.sleep(1.9)
                countstop += 1
                print(countstop)
                count = 0
                while(True):
                    if(self.car.line_detector.read_digital() != [0,0,0,0,0]):
                        break
                
            if(self.car.line_detector.read_digital() == [0,0,1,0,0]):
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [1,0,0,0,0]):
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [1,1,0,0,0]):
                self.car.steering.turn_left(65)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,1,0,0,0]):
                self.car.steering.turn_left(80)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,1,1,0,0]):
                self.car.steering.turn_left(85)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [1,1,1,0,0]):
                self.car.steering.turn_left(87)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,1,1,0]):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,1,1,1]):
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,0,1,0]):
                self.car.steering.turn_right(110)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,0,1,1]):
                self.car.steering.turn_right(115)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,0,0,1]):
                self.car.steering.turn_right(120)
                self.car.accelerator.go_forward(40)
            elif(self.car.line_detector.read_digital() == [0,0,0,0,0]):
                self.car.steering.turn(100)
                self.car.accelerator.go_backward(40)
                time.sleep(0.33)
                self.car.accelerator.stop()
            elif(self.car.line_detector.read_digital() == [1,1,1,1,1]):
                if countstop == 4:
                    self.car.accelerator.stop()
                    break
            else:
                continue
        #self.car.accelerator.stop()
                
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
myCar.drive_parking() 
