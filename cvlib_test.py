import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox
import concurrent.futures
 
url=cv2.VideoCapture(0)
# 'http://192.168.10.162/cam-hi.jpg'
im=None
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:
        # img_resp=urllib.request.urlopen(url)
        # imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        # im = cv2.imdecode(imgnp,-1)
 
        # cv2.imshow('live transmission',im)

        ret, frame = url.read()
        cv2.imshow('live transmission',frame)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
        
def run2():
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    while True:
        # img_resp=urllib.request.urlopen(url)
        # imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        # im = cv2.imdecode(imgnp,-1)
        ret, frame2 = url.read()
        img = cv2.imwrite("cvtest.png", frame2)
        img2 = cv2.imread("cvtest.png")
 
        bbox, label, conf = cv.detect_common_objects(img2)
        im = draw_bbox(img2, bbox, label, conf)

        # print(type(label))

        person = 0
        # for i in img2:
        if label==['person']:
            person += 1
        
        
        # cv2.imshow('live transmission',frame2)
        # person = 1
        # for x,y,w,h in img2:
        #     im = draw_bbox(img2, bbox, label, conf)
        #     person += 1
        
        # cv2.putText(frame2, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.putText(im, f'Total : {person}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)

        cv2.imshow('detection',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
 
 
 
if __name__ == '__main__':
    print("started")
    # while True:
    #     ret, frame = url.read()

    with concurrent.futures.ProcessPoolExecutor() as executer:
        # f1= executer.submit(run1)
        f2= executer.submit(run2)