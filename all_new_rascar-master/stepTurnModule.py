from SEN040134 import SEN040134_Tracking as Tracking_Sensor
import front_wheels

def stepTurn(detectedList):
    try:
        d = detectedList
    except:
        return 'Error!'

    sensorLists = [
        (30, [1,0,0,0,0]), (10, [1,1,0,0,0]), (10, [1,1,1,0,0]), (5, [0,1,1,0,0]), (5, [0,1,1,1,0]),
        (30, [0,0,0,0,1]), (10, [0,0,0,1,1]), (10, [0,0,1,1,1]), (5, [0,0,1,1,0]), (5, [0,1,1,1,0])
    ]

    for angle, lists in sensorLists:
        while d == lists:
            if lists[4] == 0:
                value = steering.turn_left(angle)
                print("left : ", angle)
            elif lists[0] == 0:
                value = steering.turn_right(angle)
                print("right : ", angle)
            else:
                
    return value