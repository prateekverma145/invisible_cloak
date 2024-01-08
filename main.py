import cv2 as cv

import numpy as np


def empty(a):
    pass 


# color tracker and maskcretor funtion    
def colortracker():
    cam=cv.VideoCapture(0)  # use 1 if you have external webcam
    cam.set(3,640)
    cam.set(4,480)
    cv.namedWindow('Trackbars')
    cv.resizeWindow('Trackbars',640,240)
    cv.createTrackbar('Hue Min','Trackbars',0,179,empty)
    cv.createTrackbar('Hue Max','Trackbars',179,179,empty) #adjust all these trackebar values according to the color you want to track ,thus create mask
    cv.createTrackbar('Sat Min','Trackbars',0,255,empty)
    cv.createTrackbar('Sat Max','Trackbars',255,255,empty)
    cv.createTrackbar('Val Min','Trackbars',0,255,empty)
    cv.createTrackbar('Val Max','Trackbars',255,255,empty)
    c=0
    while True:
        frame=cam.read()[1]
        frame = cv.flip(frame,1)
        h_min=cv.getTrackbarPos('Hue Min','Trackbars')
        h_max=cv.getTrackbarPos('Hue Max','Trackbars')
        s_min=cv.getTrackbarPos('Sat Min','Trackbars')
        s_max=cv.getTrackbarPos('Sat Max','Trackbars')
        v_min=cv.getTrackbarPos('Val Min','Trackbars')
        v_max=cv.getTrackbarPos('Val Max','Trackbars')
        lower=np.array([h_min,s_min,v_min])
        upper=np.array([h_max,s_max,v_max])    # after getting desired mask just note tthe values and paste it in the below code
        mask=cv.inRange(frame,lower,upper)
        mask=cv.medianBlur(mask,5)  
        mask=cv.dilate(mask,(5,5),iterations=2)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        
        key=cv.waitKey(30)
        if(key==ord('f')):
            c+=1
            cv.imwrite(f'me{c}.jpg',frame)
        if key==ord('q'):
            break
    
def invisible_cloak():   
    cam=cv.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)

    h_min,h_max,s_min,s_max,v_min,v_max=0,179,0,255,0,255
    

    result = cv.VideoWriter('filename1.avi',  
                            cv.VideoWriter_fourcc(*'MJPG'), 
                            10, (640, 480)) 
    while True:
        bg=cv.imread('me16.jpg')  # replace me6.jpg with your desired background photo
       

        frame=cam.read()[1]
           
        img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
       
        lower=np.array([0,0,52])        # here you have to paste the above all minimum noted values
        upper=np.array([25,255,255])    # same here  for max values
        mask=cv.inRange(frame,lower,upper)            
        mask=cv.medianBlur(mask,5)  
        mask=cv.dilate(mask,(5,5),iterations=2)
        ex_img=cv.bitwise_and(bg,bg,mask=mask)
        n_mask=cv.bitwise_not(mask)
        ex_frame=cv.bitwise_and(frame,frame,mask=n_mask)
      
        new_img=cv.add(ex_img,ex_frame)
        # cv.imshow('frame3',bg)
        cv.imshow('frame4',new_img)
        result.write(new_img)  # Write the frame into the file 'filename.avi'
        #cv.imshow('frame5',ex_img)
        if(key==ord('f')):
            c+=1
            cv.imwrite(f'me{c}.jpg',frame)
        
        key=cv.waitKey(30)
        if key==ord('q'):
            break

    cam.release()
    #cam1.release()

    cv.destroyAllWindows()

           
def main():
    colortracker() # comment this line after getting desired mask then execute next line 
    invisible_cloak()


if __name__ == "__main__":
    main()
            
