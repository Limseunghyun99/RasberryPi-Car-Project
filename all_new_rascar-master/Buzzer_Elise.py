import time
import RPi.GPIO as GPIO

class Elise:

    def __init__():
        # Raspberry Pi의 buzzer_pin을 8번으로 사용합니다.
        self.buzzer_pin = 8

        # BCM GPIO 핀 번호를 사용하도록 설정합니다.
        GPIO.setmode(GPIO.BOARD)

        """
        음계별 표준 주파수
        [ 도, 도#, 레, 레#, 미, 파, 파#, 솔, 솔#, 라, 라# 시], 0~11 : 2 / 12 ~ 23 : 3 / 24 ~ 35 : 4 / 36 ~ 47 :5 
        """
        self.scale = [65.4, 69.2, 73.4, 77.7, 82.4, 87.3, 92.4, 97.9, 103.8, 110, 116.5, 123.4,
                 130.8, 138.5, 146.8, 155.5, 164.8, 174.6, 184.9, 195.9, 207.6 ,220, 233, 246.9,
                 261.6, 277.1, 293.6, 311.1, 329.6, 349.2, 369.9, 391.9, 415.3, 440, 466.1, 493.8,
                 523.2, 554.3, 587.3, 622.2, 659.2, 698.4, 739.9, 783.9, 830.6, 880, 932.3, 987.7]

        """
        buzzer_pin 을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
        True 혹은 False를 쓸 수 있게 됩니다.
        """
        GPIO.setup(buzzer_pin, GPIO.OUT)

    def song_play():
        # Elise
        self.list = [40, 39, 40, 39, 40, 35, 38, 36, 33,
                9, 16, 24, 28, 33, 35, 9, 4, 8, 16, 19, 23, 24,
                4, 9, 28, 40, 39, 40, 39, 40, 35, 38, 36, 33,
                9, 16, 24, 28, 33, 35, 4, 8, 16, 36, 35, 33]


        try:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(5)     # start the PWM on 5% duty cycle

            for i in range(len(list)):
                print (i + 1)
                p.ChangeFrequency(scale[list[i]])
                if i == 8 or i == 14 or i == 21 or i == 33 or i == 39 or i == 44:
                    time.sleep(0.1)
                else:
                    time.sleep(0.2)

            p.stop()  # stop the PWM output

        finally:
            GPIO.cleanup()
