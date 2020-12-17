import os

for i in range(0, 50):
    path = '/home/har/0-code/gaze_algorithm/test_01/'
    if not os.path.exists(path+'test'+str(i)):
        os.makedirs(path+'orbbec_frame/test'+str(i))
        # os.makedirs(path + 'orbbec_frame_npy/test' + str(i))
        os.makedirs(path + 'glasses_frame/test' + str(i))
        os.makedirs(path + 'orbbec_gaze_2D/test' + str(i))
        os.makedirs(path + 'orbbec_gaze_3D/test' + str(i))
        os.makedirs(path + 'web_camera_1/test' + str(i))
        os.makedirs(path + 'web_camera_2/test' + str(i))

print('finished')