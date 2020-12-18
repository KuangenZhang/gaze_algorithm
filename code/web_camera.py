import cv2
import time
import os
import sys

file_path = '/home/har/0-code/gaze_algorithm/test_01'
ns = sys.argv[1]
# ns = 0``
print("tobii_gaze")
print(ns)

cap_list = []
for id in [2, 4]:
    cap = cv2.VideoCapture(id) #计算机自带的摄像头为0，外部设备为1
    cap_list.append(cap)
    print(cap)
while(1):
    t = time.time()
    for i in range(2):
        ret,frame = cap_list[i].read()  #ret:True/False,代表有没有读到图片  frame:当前截取一帧的图片
        if ret:
            cv2.imshow("web camera {}".format(i + 1),frame)
            web_camera_img_name = '{}/test{}/web_camera_{}/{:.3f}.jpg'.format(file_path, ns, i+1, t)
            cv2.imwrite(web_camera_img_name, frame)
            print('web camera saved')
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()