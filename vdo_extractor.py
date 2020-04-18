import os
import cv2

try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print('Error: can not create a directory of frames.')

vdo_name = str(input("Input VDO's name (ex. file_name.mp4): "))
# vdo_name = 'val_asm_v2.mp4'

# print(vdo_name.split('.')[0])

vdo_name.split('.')[0]

if os.path.isfile(vdo_name):
    vdocap = cv2.VideoCapture(vdo_name) # file_name.mp4
    count = 0

    # every_n_frame = 1 # 1 means every frame
    every_n_frame = int(input("extract frame every n frames (means every frame): "))

    while True:
        nth_frame = vdocap.get(cv2.CAP_PROP_POS_FRAMES) # current frame, which start with 0
        ret,frame = vdocap.read()

        if not ret:
            break

        # extract a frame every n frames
        if nth_frame % every_n_frame == 0:
            file_name = './frames/' + vdo_name.split('.')[0] + '_frame_' + str(count) + '.jpg'
            cv2.imwrite(file_name, frame)
            print('Create frame_%d.jpg' % count)
            count += 1

    print('DONE!!')

else:
    print('Error: cannot find %s.' % vdo_name)