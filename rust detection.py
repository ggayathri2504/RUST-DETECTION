
# import the necessary packages
from skimage.measure import compare_ssim
import imutils
import cv2
import sqlite3 as sq
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import database as db

#extracting image from video
imageA = cv2.imread('normal_image.jpeg')
imageB = cv2.imread('hsv_image.jpeg')

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
  
# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)

#exporting rust detected points to database
arr = np.array(thresh)
my_list=[]
i_ele=[]
j_ele=[]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j]==255:
            i_ele.append(i)
            j_ele.append(j)
            my_list.append([i,j])

print(my_list)

#maintable insertion
date = dt.datetime.now()
db.maintable_insertion(date.date(),dt.datetime.now().strftime("%H:%M:%S"))
#x,y points insertion
for i in range(len(i_ele)):
    db.x_insertion(i_ele[i],j_ele[i])
        
#plotting the points to see accurate 
plt.scatter(i_ele,j_ele)
plt.show()

#closing the files
key = cv2.waitKey(0)
cv2.destroyAllWindows()
