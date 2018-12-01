from SEN040134 import SEN040134_Tracking as Tracking_Sensor
import time
import RPi.GPIO as GPIO

if __name__ == "__main__":
    Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
    try:
        while True:
            print("Current detection result: :", Tracker.read_digital())
            print("The result of the driver detecting the line : ", Tracker.is_in_line())
            print("The result of detecting the center of the line :", Tracker.is_center())
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
