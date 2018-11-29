# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
# import ALL method in the SEN040134 Tracking Module
# =======================================================================
from SEN040134 import SEN040134_Tracking as Tracking_Sensor

# =======================================================================
# import ALL method in the TCS34725 RGB Module
# =======================================================================
from TCS34725 import TCS34725_RGB as RGB_Sensor

# =======================================================================
# import ALL method in the SR02 Ultrasonic Module
# =======================================================================
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor

# =======================================================================
# import ALL method in the rear/front Motor Module
# =======================================================================
import rear_wheels
import front_wheels
# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)


class Car(object):

    def __init__(self):
        self.moduleInitialize()

    def drive_parking(self):
        # front wheels center allignment
        self.front_steering.turn_straight()

        # power down both wheels
        self.rear_wheels_drive.stop()
        self.rear_wheels_drive.power_down()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def assignment_main(self):
        #=================================================================
        #Variable
        #=================================================================

        handle = front_wheels.Front_Wheels(db = 'config')
        #초음파 센서로 부터 거리값을 받아와 distance에 저장합니다.
        distance = self.distance_detector.get_distance()
        #뒷바퀴 오브젝트를 accelerator로 받아옵니다.
        accelerator = rear_wheels.Rear_Wheels(db='config')
        #뒷바퀴를 준비시킵니다.
        accelerator.ready()
        #시간 측정을 위해 시간을 저장합니다.
        start_time = time.time()
        #거리가 아직 먼 경우에 반복하고 너무 먼 경우 -1이 리턴 되므로 하나의 경우를 더 처리합니다.
        while(distance >25 or distance < 0):
            #70의 속도로 전진합니다.
            accelerator.forward_with_speed(70)
            #distance값을 계속 받아옵니다.
            distance = self.distance_detector.get_distance()
            #간격을 두지 않았더니 값이 계속 튀어서 0.2초의 간격을 두었습니다.
            time.sleep(0.20)
            #에코 체킹을 위해 거리값을 출력합니다.
            print(distance)
            #만약 거리가 너무 가가까워진 경우
            if(distance < 25 and distance >0):
                #사용자에게 거리가 가까움을 출력합니다.
                print("Too close")
                #진행하는 동안 걸린 시간을 측정합니다,
                end_time = time.time()
                #차를 멈추고
                accelerator.stop()
                #후진
                accelerator.backward_with_speed(80)
                #주행하는데 걸린 시간만큼 후진합니다.
                time.sleep(end_time - start_time)
                #정지
                accelerator.stop()
                #앞바퀴 정렬
                handle.turn_straight()



    def moduleInitialize(self):
        try:
            # ================================================================
            # ULTRASONIC MODULE DRIVER INITIALIZE
            # ================================================================
            self.distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)

            # ================================================================
            # TRACKING MODULE DRIVER INITIALIZE
            # ================================================================
            self.line_detector = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])

            # ================================================================
            # RGB MODULE DRIVER INITIALIZE
            # ================================================================
            self.color_getter = RGB_Sensor.TCS34725()

            # ================================================================
            # FRONT WHEEL DRIVER SETUP
            # ================================================================
            self.front_steering = front_wheels.Front_Wheels(db='config')
            self.front_steering.ready()

            # ================================================================
            # REAR WHEEL DRIVER SETUP
            # ================================================================
            self.rear_wheels_drive = rear_wheels.Rear_Wheels(db='config')
            self.rear_wheels_drive.ready()

            # ================================================================
            # SET LIMIT OF TURNING DEGREE
            # ===============================================================
            self.front_steering.turning_max = 35

            # ================================================================
            # SET FRONT WHEEL CENTOR ALLIGNMENT
            # ================================================================
            self.front_steering.turn_straight()

            # ================================================================
            # DISABLE RGB MODULE INTERRUPTION
            # ================================================================
            self.color_getter.set_interrupt(False)

        except:
            print("MODULE INITIALIZE ERROR")
            print("CONTACT TO Kookmin Univ. Teaching Assistant")


if __name__ == "__main__":
    try:
        car = Car()
        car.assignment_main()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        car.drive_parking()
