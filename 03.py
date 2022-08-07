import numpy as np
import cv2 as cv
# cap = cv.VideoCapture(0)
cap = cv.VideoCapture("C:/003/video1.MTS")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    # cv.imshow('frame', gray)
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):  #按Q結束
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()