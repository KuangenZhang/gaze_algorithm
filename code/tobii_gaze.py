#!/usr/bin/python3

import cv2
import numpy as np
import time
import os
from tobiiglassesctrl import TobiiGlassesController
import sys

file_path = '/home/har/0-code/gaze_algorithm/test_01'

ns = sys.argv[1]
print("tobii_gaze")
print(ns)
# print("file_path: ", os.getcwd() + file_path)


if hasattr(__builtins__, 'raw_input'):
    input = raw_input

ipv4_address = "192.168.71.50"

tobiiglasses = TobiiGlassesController(ipv4_address, video_scene=True)
# print(tobiiglasses.get_battery_info())
# print(tobiiglasses.get_storage_info())

project_id = tobiiglasses.create_project("Test live_scene_and_gaze.py")

participant_id = tobiiglasses.create_participant(project_id, "participant_test")

calibration_id = tobiiglasses.create_calibration(project_id, participant_id)

input("Put the calibration marker in front of the user, then press enter to calibrate")
tobiiglasses.start_calibration(calibration_id)

res = tobiiglasses.wait_until_calibration_is_done(calibration_id)

if res is False:
    print("Calibration failed!")
    exit(1)

cap = cv2.VideoCapture("rtsp://%s:8554/live/scene" % ipv4_address)
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed
tobiiglasses.start_streaming()
print("Start streaming. Please wait ...")

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        height, width = frame.shape[:2]
        t = time.time()
        data_gp = tobiiglasses.get_data()['gp']
        data_gp_3D = tobiiglasses.get_data()['gp3']

        # {u's': 0, u'gp': [0.4447, 0.0811], u'gidx': 9958, u'ts': 416651015, u'l': 67277}
        # {u's': 0, u'gidx': 9961, u'ts': 416711002, u'gp3': [45.04, 173.8, 464.21]}
        # -----------
        if data_gp['ts'] > 0:
            gaze_2d_name = '{}/test{}/orbbec_gaze_2D/{:.3f}.npy'.format(file_path, ns, t)
            np.save(gaze_2d_name, data_gp['gp'])

            cv2.circle(frame, (int(data_gp['gp'][0] * width), int(data_gp['gp'][1] * height)), 30, (0, 255, 0), 10)
            cv2.namedWindow('Tobii Pro Glasses 2 - Live Scene', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Tobii Pro Glasses 2 - Live Scene', 960, 540)
            cv2.imshow('Tobii Pro Glasses 2 - Live Scene', frame)
            glasses_frame_name = '{}/test{}/glasses_frame/{:.3f}.jpg'.format(file_path, ns, t)
            cv2.imwrite(glasses_frame_name, cv2.resize(frame, (192, 108)))

            print('gaze_saved')
        if data_gp_3D['ts'] > 0:
            gaze_3d_name = '{}/test{}/orbbec_gaze_3D/{:.3f}.npy'.format(file_path, ns, t)
            np.save(gaze_3d_name, data_gp_3D['gp3'])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

tobiiglasses.stop_streaming()
tobiiglasses.close()
