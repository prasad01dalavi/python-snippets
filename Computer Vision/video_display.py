import cv2          # Import open cv
import time
video_file1 = '/media/prasad/Programming/Codes/Python/Modules/Computer Vision/nature.mp4'
video_file2 = '/home/prasad/Downloads/test.3gp'

cap = cv2.VideoCapture('nature.mp4')

ret, frame = cap.read()
print 'Read data:', ret, frame
while True:
    ret, frame = cap.read()
    # Converts color image to grayscale
    # grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == True:
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        print 'No frame!'
        break

cap.release()
cv2.destroyAllWindows()
