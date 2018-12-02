#########################################################################
# Date: 2018/09/07
# file name: GPIO_LED_On_Off_Example.py
# Purpose: this code has been generated for control LED Module
# if this program is run then LED will blink 1Hz
#########################################################################

# coding=utf-8
"""
LED를 제어하기 위해 RPi.GPIO 모듈을 GPIO로 import 합니다.
sleep 함수를 사용하기 위해서 time 모듈을 import 합니다.
"""

import time
import RPi.GPIO as GPIO


class Led:
    def __init__(self):
        # Raspberry Pi 보드의 led_pin을 사용합니다.
        self.led_pinR = 37

        # Raspberry Pi 보드 핀 순서를 사용하도록 설정합니다.
        GPIO.setmode(GPIO.BOARD)

        """
        led_pin을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
        True 혹은 False를 쓸 수 있게 됩니다.
        """
        GPIO.setup(led_pinR, GPIO.OUT)

    def on_off(self, frequency):
        #  1s = 1000ms
        while True:
            # led_pin 에 연결된 LED 가 켜집니다.
            GPIO.output(self.led_pinR, True)
            time.sleep(frequency)  # 500ms
        
            # led_pin 에 연결된 LED 가 꺼집니다.
            GPIO.output(self.led_pinR, False)
            time.sleep(frequency)  # 500ms

        GPIO.cleanup()

"""
control + c 키를 눌러서 KeyboardInterrupt를 발생시키면
GPIO.cleanup()을 호출하여 GPIO를 초기 상태로 돌려놓습니다.
"""
