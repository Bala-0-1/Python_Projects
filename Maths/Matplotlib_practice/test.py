
#Importing openCv both as cv2 and cv for better convinence 
import cv2  
import cv2 as cv 

import urllib

# Importing numpy for working with numpy arrays
import numpy as np 

# Importing pyplot as plt from maplotlib for Image Visualization
from matplotlib import pyplot as plt 

#Collab not support cv2.imshow method thus, importing cv2.imshow method for better Image visualization 
#from google.colab.patches import cv2_imshow  

#Importing PIL library for working with Images
from PIL import Image 

#Importing asarray method from numpy for dealing with pixels of Images
from numpy import asarray 

import matplotlib.image as mpimg

#Importing ndimage from scipy as this package contains various functions for multidimensional image processing.
from scipy import ndimage

#Importing filters, features, measures and color from skimage
from skimage import filters, feature, measure, color

#Importing Watershed for touching Grains sepration
from skimage.segmentation import watershed


#Defining show function for displaying  image with custom X and Y cordinates

def show(image,x=30,y=7):
#   img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  plt.figure(figsize=(x,y))
  plt.imshow(image,cmap="gray")
  
  
  #Reading Image
img = cv2.imread("/Users/balakumaranb/Downloads/grains.jpg")

#Using predefined show function for displaying the image
show(img,20,7)



#Converting Image BGR Image to Gray for Image thresholding and further Image-Preprocessing application
grayscale_Image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
th, thresh_img = cv.threshold(grayscale_Image, 120, 255, cv.THRESH_BINARY)

show(thresh_img)

#Using show function earlier defined
# show(thresh_img)


# Noise removal
kernel = np.ones((3),np.uint8)
clear_image = cv.morphologyEx(thresh_img,cv.MORPH_OPEN, kernel, iterations=8)

#Using show function earlier defined
show(clear_image)


contours, hierarchy = cv.findContours(clear_image, 
                                          cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

output_contour = cv.cvtColor(clear_image, cv.COLOR_GRAY2BGR)
cv.drawContours(output_contour, contours, -1, (255, 0, 0), 2)
show(output_contour)


#Applying Countours method to get the count of rice grains
contours, hierarchy = cv.findContours(clear_image, 
                                      cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


output_contour = cv.cvtColor(clear_image, cv.COLOR_GRAY2BGR)
cv.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
print("Number of detected contours", len(contours))



#To visualize the segmentation conveniently, There needed a colour-code the labelled regions using the color, thus I did it.


#Applying  distance_transform_edt to computes the distance from non-zero (i.e. non-background) points to the nearest zero (i.e. background) point.
dist_trans = ndimage.distance_transform_edt(clear_image)

#Applying peak_local_max function for getting coordinates of local peaks (maxima) in an image.
local_max = feature.peak_local_max(dist_trans, min_distance=23)


local_max_mask = np.zeros(dist_trans.shape, dtype=bool)
local_max_mask[tuple(local_max.T)] = True

#Aplying Watershed algorithm
labels = watershed(-dist_trans, measure.label(local_max_mask), mask=clear_image) # separate merged corns

Rice_area = []
unique_labels = np.unique(labels)
for label in unique_labels:
    if label == 0:  # Exclude the background label
        continue
    object_mask = labels == label
    area = np.sum(object_mask)
    if area < 50: # filter out small contours
        continue
    eq_diameter = np.sqrt(4 * area / np.pi)

    # Convert the equivalent diameter to millimeters
    #pixel_size = 0.10  # assume each pixel is 0.014 mm (you can adjust this based on your image)
    eq_diameter_mm = eq_diameter * 0.09
    Rice_area.append(round(eq_diameter_mm,3))


#label2rgb function, specifying the background label with argument bg_label=0.
plt.figure(figsize=(30,10))
plt.imshow(color.label2rgb(labels, bg_label=0))
print("Number of Rice grains are : %d" % labels.max())


print("\n\nTotal rice grain count as per contour is: ",len(Rice_area))

print("\n")

TotalRiceAreaSum=0
for count in range(0,len(Rice_area)):
    print("Area of the rice grain",count+1, "is:",Rice_area[count],"mm")
    
    

#Broken Rice count
BrokenRiceCount=0
brokenRiceArea=0
TotalRiceAreaSum=0
for rice in Rice_area:
    TotalRiceAreaSum+=rice
    if rice < 1.5:
        brokenRiceArea+=rice
        BrokenRiceCount+=1
        
print("\nRice Analysis :")

print("Total rice count is",len(Rice_area))
    #Average area of rice 
print("Average area of rice is: ", round(TotalRiceAreaSum/len(Rice_area),3)," mm")

print("Broken Rice count is: ",BrokenRiceCount)

#Percentage of rice grain Broken
print("Percentage of rice grain broken is :",round((brokenRiceArea/len(Rice_area)+brokenRiceArea),3),"% percent")
