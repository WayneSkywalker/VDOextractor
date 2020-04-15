import os
import cv2

try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print('Error: can not create a directory of frames.')

vdocap = cv2.VideoCapture('val_asm_v2.mp4') # file_name.mp4
count = 0

every_n_frame = 1 # 1 means every frame

while True:
    nth_frame = vdocap.get(cv2.CAP_PROP_POS_FRAMES) # current frame, which start with 0
    ret,frame = vdocap.read()

    if not ret:
        break

    # extract a frame every n frames
    if nth_frame % every_n_frame == 0:
        cv2.imwrite('./frames/frame_%d.jpg' % count, frame)
        print('Create frame_%d.jpg' % count)
        count += 1