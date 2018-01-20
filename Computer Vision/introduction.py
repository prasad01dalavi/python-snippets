import cv2          # Import open cv
import time
image_path = '/media/prasad/Programming/Codes/Python/Modules/Computer Vision/my_bike.jpg'
# Reading the image in colored foramat

color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
# this will return an array of pixel value 0 to 255 for RGB

grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Reading the image in grayscale format 0->black, 255->white

color_image_resize1 = cv2.resize(color_image, (600, 400))  # Resizing the read image to display
cv2.imshow("My Colored Bike ", color_image_resize1)        # Display the colored image

color_image_resize2 = cv2.resize(grayscale_image, (600, 400))  # Resizing the read image to display
cv2.imshow("My Grayscaled Bike ", color_image_resize2)         # Display the colored image

cv2.waitKey(0)          # Do not exit until I press any waitKey (it is like getch())
cv2.destroyAllWindow()  # Close all windows
