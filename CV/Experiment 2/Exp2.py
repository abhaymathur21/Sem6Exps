
import numpy as np
import cv2 as cv
img = cv.imread('photo.jpg', 0)
cv.imshow('Original',img)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('Translated image', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()
M = np.float32([[1,  0, 0],
                [0, -1, rows],
                [0,  0, 1]])
Xreflected_img = cv.warpPerspective(img, M,(int(cols),int(rows)))
cv.imshow('Vertical Reflected Image',Xreflected_img)
M = np.float32([[-1, 0, cols],
                [0, 1, 0],
                [0, 0, 1]])
Yreflected_img = cv.warpPerspective(img, M,(int(cols),int(rows)))
cv.imshow('Horizontal Reflected Image', Yreflected_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
img_rotation = cv.warpAffine(img,cv.getRotationMatrix2D((cols/2, rows/2),30,0.8),(cols, rows))
cv.imshow('Rotated image', img_rotation)
# cv.waitKey(0)
# cv.destroyAllWindows()
M=np.float32([[0.5,0,0],[0,0.5,0]])
img_shrinked = cv.warpAffine(img,M,(int(cols), int(rows)))
cv.imshow('Shrinked image', img_shrinked)
M=np.float32([[1.5,0,0],[0,1.5,0]])
img_enlarged = cv.warpAffine(img,M,(int(cols*1.5), int(rows*1.5)))
cv.imshow('Enlarged image', img_enlarged)
# cv.waitKey(0)
# cv.destroyAllWindows()
cropped_img = img[100:300, 100:300]
cv.imshow('Cropped Image', cropped_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('Shear(Xaxis) img', sheared_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
M = np.float32([[1,   0, 0], [0.5, 1, 0], [0,   0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('shear(Yaxis)', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()