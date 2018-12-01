from SR02 import SR02_Supersonic as Supersonic_Sensor
import time

if __name__ == "__main__":
    print('DETECTED')
    supersonic_pin = 35
    print(supersonic_pin)
    detector = Supersonic_Sensor.Supersonic_Sensor(supersonic_pin)
    while True:
        print(detector.get_distance())
        time.sleep(0.4)
