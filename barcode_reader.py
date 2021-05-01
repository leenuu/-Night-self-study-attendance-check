import pyzbar.pyzbar as pyzbar 
import numpy as np 
import cv2
from test import *
def cam():
    capture = cv2.VideoCapture(1)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    while True:
        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)
        if cv2.waitKey(1) > 0:
            break


    capture.release()
    cv2.imwrite('barcode.png',frame, params=[cv2.IMWRITE_JPEG_QUALITY,0])
    cv2.destroyAllWindows()
    #test.predict()

cam()
def decode(im):
    decodedObjects = pyzbar.decode(im) 
        
    for obj in decodedObjects: 
        print('Type : ', obj.type) 
        print('Data : ', obj.data, '\n') 
        
    return decodedObjects

def display(im, decodedObjects):  
    for decodedObject in decodedObjects: 
        points = decodedObject.polygon
        if len(points) > 4: 
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32)) 
            hull = list(map(tuple, np.squeeze(hull))) 

        else:
            hull = points; 
                
            
        n = len(hull) 
            
        for j in range(0, n): 
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3) 
                
        #cv2.imshow('barcode', im)
        #cv2_imshow(im)
        #cv2.waitKey(0)
        
if __name__ == '__main__': 
    im = cv2.imread('barcode.png') 
    #im = cv2.imread('barcode.jpg', cv2.IMREAD_UNCHANGED)
            
    decodedObjects = decode(im)
    display(im, decodedObjects)
