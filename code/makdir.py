import os

for i in range(0, 50):
    path = '/home/har/0-code/gaze_algorithm/test_01/'
    os.makedirs(path + 'test{}/glasses_frame'.format(i))
    os.makedirs(path + 'test{}/orbbec_rgb'.format(i))
    os.makedirs(path + 'test{}/orbbec_depth'.format(i))
    os.makedirs(path + 'test{}/orbbec_gaze_2D'.format(i))
    os.makedirs(path + 'test{}/orbbec_gaze_3D'.format(i))
    os.makedirs(path + 'test{}/web_camera_1'.format(i))
    os.makedirs(path + 'test{}/web_camera_2'.format(i))
print('finished')