#########################################################################
# Date: 2018/10/12
# file name: 1st_20181667_이예슬.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
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
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

        # config 파일로부터 calibration 된 값을 가져와 앞바퀴 정렬
        steering = front_wheels.Front_Wheels(db = 'config')
        steering.center_alignment()

        # config 파일로부터 뒷바퀴 방향 값을 가져옴으로써 구동체 출발 준비 완료
        accelerator = rear_wheels.Rear_Wheels(db = 'config')
        accelerator.ready()

        # 초음파 센서의 하드웨어적 문제를 해결하기 위해 작성한 에러처리 코드에 필요한 변수
        current = 0
        previous = 0

        # 시간 측정 시작
        start_time = time.time()

        # 구동체 속도 100으로 출발
        accelerator.go_forward(95)


        while True:
            # 5번의 거리 측정값을 변수로 지정
            measurement1 = distance_detector.get_distance()
            measurement2 = distance_detector.get_distance()
            measurement3 = distance_detector.get_distance()
            measurement4 = distance_detector.get_distance()
            measurement5 = distance_detector.get_distance()

            # 에러처리를 위한 코드 부분
            # 거리 측정값들을 리스트에 담은 뒤 정렬함
            distances = [measurement1, measurement2, measurement3, measurement4, measurement5]
            sorted_distances = sorted(distances)
            # 절사평균을 구하기 위해 양 끝 값을 제거함
            del sorted_distances[0]
            del sorted_distances[3]
            # 절사평균 구함
            average = (sorted_distances[0] + sorted_distances[1] + sorted_distances[2])//3

            # 에러처리 확인을 위해 측정된 거리 값 출력
            print("Distance : ", average)
            time.sleep(0.0001)

            # 현재 측정된 값이 직전 측정값에 비해 30이상 차이나면 현재 측정값 대신 이전 측정값을 진짜 측정값으로 처리함
            #if current < (previous - 25) or current > (previous + 25):
                #current == previous

            # 측정된 거리 값이 40에서 60 사이면 속도를 100에서 95로 줄임
            if 40 < average <= 60:
                accelerator.go_forward(95)

            # 측정된 거리 값이 20에서 40 사이면 속도를 95에서 90으로 줄임
            elif 20 < average <= 40:
                accelerator.go_forward(90)

            # 측정된 거리 값이 0에서 10 사이면 정지한 후 앞바퀴 정렬을 다시함
            elif 0 < average <= 11:
                accelerator.stop()
                steering.center_alignment()
                time.sleep(0.1)
                stop_time = time.time()# 정지했을 때의 시간 측정
                time.sleep(0.01)
                break# 위 과정이 끝나면 반복문을 빠져나감

            # 그 외의 값들은 무시하고 반복문의 내용을 처리함
            else:
               continue

        # 75의 속도로 멈춘 시간에서 출발한 시간을 뺀 만큼 후진함
        accelerator.go_backward(75)
        time.sleep(stop_time-start_time)

        # 후진이 끝나면 정지한 후 종료함
        accelerator.stop()
        accelerator.power_down()


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
