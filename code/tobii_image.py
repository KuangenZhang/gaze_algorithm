#!/usr/bin/python3

import cv2
import numpy as np
import time
from tobiiglassesctrl import TobiiGlassesController
import sys

ns = sys.argv[1]
print("tobii_image")
print(ns)
file_path = '/home/har/0-code/gaze_algorithm/test_01'

if hasattr(__builtins__, 'raw_input'):
    input = raw_input

ipv4_address = "192.168.71.50"

tobiiglasses = TobiiGlassesController(ipv4_address, video_scene=True)
# print(tobiiglasses.get_battery_info())
# print(tobiiglasses.get_storage_info())


cap = cv2.VideoCapture("rtsp://%s:8554/live/scene" % ipv4_address)
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
tobiiglasses.start_streaming()
print("Start streaming. Please wait ...")
# time.sleep(3.0)

i = 0
timeF = 10

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        height, width = frame.shape[:2]
        i = i + 1
        data_gp = tobiiglasses.get_data()['gp']
        data_gp_3D = tobiiglasses.get_data()['gp3']
        cv2.circle(frame, (int(data_gp['gp'][0] * width), int(data_gp['gp'][1] * height)), 30, (0, 0, 255), 5)
        cv2.namedWindow('Tobii Pro Glasses 2 - Live Scene', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Tobii Pro Glasses 2 - Live Scene', 640, 480)
        cv2.imshow('Tobii Pro Glasses 2 - Live Scene', frame)
        cv2.waitKey(1)
        if (i % timeF == 0):
            print(i)
            t = time.time()
            # frame = cv2.resize(frame, (192, 108))
            cv2.imwrite(
                file_path + '/glasses_frame/test' + str(ns) + '/' + '{:.3f}'.format(t) + '.jpg',
                frame)
            print('glasses frame saved')
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

tobiiglasses.stop_streaming()
tobiiglasses.close()
