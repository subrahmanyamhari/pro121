# import cv2 to capture videofeed
import cv2
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount everest.jpg')

# resizing the mountain image as 640 X 480
mountain = cv2.resize(mountain, (640, 480))


while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
        mount_rgb = cv2.cvtColor(mountain, cv2.COLOR_BGR2RGB)
        # creating thresholds
        lower_bound = np.array([200,200,200])
        upper_bound = np.array([255,255,255])
        # thresholding image
        mask1 = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        mask2 = cv2.bitwise_not(mask1)
        r = cv2.bitwise_and(frame, frame, mask=mask2)
        r1 = cv2.bitwise_and(mountain, mountain, mask=mask1)
        # final image
        output = cv2.addWeighted(r, 1, r1, 1, 0)
        # show it
        cv2.imshow('frame' , output)
        cv2.imshow("mask", mask1)
        cv2.imshow("mask1",mask2)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
