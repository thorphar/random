# Conda install list
# conda install -c conda-forge ocl-icd-system 
# conda install -c conda-forge pyopencl
# conda install -c conda-forge pocl
# conda install -c conda-forge opencv
import cv2
import pyopencl as cl


if __name__ == "__main__":
    img = cv2.imread('/home/thorphar/Pictures/beans.jpg',0) # reads image 'opencv-logo.png' as grayscale
    sel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    img = cv2.erode(img,sel,iterations = 1)
    img = img + 100 
    img = cv2.dilate(img,sel,iterations = 10)

    cv2.imshow("Beans", img)
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()