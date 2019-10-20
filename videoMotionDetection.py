from __future__ import print_function
import cv2 as cv
import argparse

# VideoMotionDetection.py
# Simple OpenCV script 

# Arguments handling, not much use as of now but will be 
# to set video recording interval, threashold for detecting motion 
# and so on.

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. Video stream is taken from first system camera (device 0).')

parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

# createBackgroundSubtractor*() parameters:
#   - history (def 500): how many frames from history to take into account
#   - dist2Threashold (def 400.0): threashold on the squred distance, need to check better
#   - detectShadows (true): detects shadows with a different color, slows down things a bit

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2(150, 200.0, 0)
else:
    backSub = cv.createBackgroundSubtractorKNN(150, 200.0, 0)

# Start video capture, if only 1 camera in availble, 
# this is device 0.

capture = cv.VideoCapture(0)
if not capture.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)

# Screenshot flag is initially set to False, to avoid
# screenshot being saved in the first few seconds of camera capture, 
# which always have a lot of whites. 

screenshotFlag = False
imgCount = 0

# Main loop

while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)

# I want not to count how many white pixels we have in the mask
# which I can hopefully use as rough indication of how much
# stuff was actually moving over there.

    print("Number of white pixels in mask: ", cv.countNonZero(fgMask))

    if (cv.countNonZero(fgMask)) > 250 and screenshotFlag:

            filename = "screenshot_" + str(imgCount) + ".png"
            # Take a screenshot from the camera
            cv.imwrite(filename, frame)
            print("Screenshot has been saved!")
            imgCount += 1

#    contours = cv.findContours(fgMask,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

#    print("Debug for contours structure: ")
#    print(contours)


#    cv.rectangle(frame, contours[1][0], (255,255,255), -1)
#    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
#               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
#    
#    
#    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    
    pressedKey = cv.waitKey(1)

    if pressedKey & 0xFF == ord('q'):
        break

    elif pressedKey & 0xFF == ord('s'):
        screenshotFlag = not screenshotFlag
        print("\n\nScreenshot flag has been set to: ", screenshotFlag)

capture.release()
cv.destroyAllWindows()
