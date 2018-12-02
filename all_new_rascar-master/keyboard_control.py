# file name: 3rd_assignment_main.py Purpose: this code has been 
# generated for the 4 wheel drive body moving object to perform the 
# project with line detector this code is used for the student only
#########################################################################
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages')
import Buzzer_Yes
import Led_module_Yes
from car import Car
import time
import keyboard



class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        #self.car.steering.turning_max = 50
        self.color = self.car.color_getter
        self.line = self.car.line_detector
        self.average_speed = 75
        self.flag = True
        self.dead_flag = True
        self.finished = False
        self.buzzer = Buzzer_Yes.Buzz()
        self.led = Led_module_Yes.Led()

    def keyboard_control(self):
        while True:
            if keyboard.is_pressed('w'):
                if keyboard.is_pressed('a'):
                    self.car.steering.turn(75)
                    self.car.accelerator.go_forward(70)
                    continue
                elif keyboard.is_pressed('d'):
                    self.car.steering.turn(105)
                    self.car.accelerator.go_forward(70)
                    continue
                else:
                    self.car.steering.turn(90)
                    self.car.accelerator.go_forward(70)
                    continue

            elif keyboard.is_pressed('s'):
                if keyboard.is_pressed('a'):
                    self.car.steering.turn(75)
                    self.car.accelerator.go_backward(70)
                    continue
                elif keyboard.is_pressed('d'):
                    self.car.steering.turn(105)
                    self.car.accelerator.go_backward(70)
                    continue
                else:
                    self.car.steering.turn(90)
                    self.car.accelerator.go_backward(70)
                    continue
            elif keyboard.is_pressed('a'):
                self.car.steering.turn(65)
                self.car.accelerator.go_forward(70)
                continue

            elif keyboard.is_pressed('d'):
                self.car.steering.turn(115)
                self.car.accelerator.go_forward(70)
                continue

            elif keyboard.is_pressed('q'):
                self.car.accelerator.leftLarge()
                continue

            elif keyboard.is_pressed('e'):
                self.car.accelerator.rightLarge()
                continue

            else:
                self.car.accelerator.stop()




    def drive_parking(self):
        self.car.drive_parking()

    def side_parking(self):
        self.adequate_time = 1.8
        self.car.steering.turn(110)
        self.car.accelerator.go_forward(60)
        time.sleep(0.4)
        self.car.accelerator.stop()
        self.car.steering.turn(90)
        #self.car.accelerator.go_backward(30)
        #time.sleep(0.6)
        self.car.accelerator.leftLarge()
        time.sleep(self.adequate_time-0.2)
        self.car.accelerator.stop()
        time.sleep(1)
        self.car.steering.turn(70)
        self.car.accelerator.leftLarge()
        time.sleep(self.adequate_time)
        #self.car.steering.turn(70)
        self.car.steering.turn(85)
        self.car.accelerator.go_forward(60)
        time.sleep(1)
        
        self.car.accelerator.stop()

    def line_tracing(self):
        if self.line.read_digital() == [0, 0, 1, 0, 0]:
            self.car.accelerator.go_forward(self.average_speed)
            
        elif self.line.read_digital() == [0,1,1,1,1] :
            self.car.steering.turn(70)
            self.car.accelerator.go_forward(self.average_speed)

        elif self.line.read_digital()[0] == 1 :
            self.car.steering.turn(65)
            self.car.accelerator.go_forward(self.average_speed)
            return

        elif self.line.read_digital()[1] == 1:
            self.car.steering.turn(80)
            self.car.accelerator.go_forward(self.average_speed)
            return

        elif self.line.read_digital()[3] == 1:
            self.car.steering.turn(100)
            self.car.accelerator.go_forward(self.average_speed)
            return

        elif self.line.read_digital()[4] == 1:
            self.car.steering.turn(110)
            self.car.accelerator.go_forward(self.average_speed)
            return

        elif self.line.read_digital() == [0, 0, 0, 0, 0]:
            self.car.steering.turn(110)
            self.car.accelerator.go_backward(40)
            return
            #time.sleep(0.33)
            #self.car.accelerator.stop()

        elif self.car.line_detector.read_digital() == [1, 1, 1, 1, 1] :
            self.car.accelerator.stop()
            if self.flag and self.dead_flag :
                 self.finished = True
            return
            #time.sleep(10)

        else:
            self.car.steering.turn(90)
            self.car.accelerator.go_forward(self.average_speed)
            time.sleep(0.05)
            pass
        

    def avoidence(self):
        self.dead_flag = False
        self.car.accelerator.stop()
        self.car.steering.turn(70)
        self.car.accelerator.go_forward(70)
        time.sleep(0.4)
        while self.car.line_detector.read_digital() != [1, 0, 0, 0, 0]:
            self.car.accelerator.go_forward(70)
        self.car.steering.turn(120)
        self.car.accelerator.go_forward(70)
        time.sleep(1)
        while self.car.line_detector.read_digital()[4] == 0:
            self.car.accelerator.go_forward(70)

    def car_startup(self):
        self.car.accelerator.go_forward(60)
        while True:
            print("tracking: ", self.car.line_detector.read_digital())
            distance = self.car.distance_detector.get_distance()
            print("distance: ", distance)
            print("")
            if self.finished:
                print("Finished")
                break
            temp = []

            self.line_tracing()
            # prevent distance value error
            for i in range(5):
                distance = self.car.distance_detector.get_distance()
                temp.append(distance)
                temp.sort()

            # 장애물 회피
            if 0 < temp[2] < 31 and self.dead_flag:
                self.avoidence()

            # 신호등
            if self.car.color_getter.red_signal() and self.flag:
                self.car.accelerator.stop()
                print("Red, stop")
                self.flag = False
                time.sleep(1)

            #바닥 인식
            if self.car.color_getter.green_signal():
                frequency = self.color.color_to_frequency()
                self.car.steering.turn(65)
                self.buzzer.on_off(frequency)
                self.led.on_off(frequency)

            #평면 주차
            if self.car.color_getter.blue_signal():
                self.side_parking()   
            

            





if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.keyboard_control()
        #myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
