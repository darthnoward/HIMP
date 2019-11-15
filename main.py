#! /usr/bin/python3 
# dependencies: Python3, OpenCV, imagemagick, xclip (for copying only)

import numpy as np 
import cv2 
from datetime import datetime
from os import system

window = datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "   HIMP  Haolan Image Manipulation Program"

def dummy():
    pass

font = cv2.FONT_HERSHEY_SIMPLEX

def onClick(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONUP:
        click.pop()
        tmp = frames[-1]
        if param[0] == 'blur':
            frames.pop()
            [x1, y1] =  position[0]
            tmp = frames[-1].copy()
            region = tmp[min(y1,y):max(y1,y), min(x1,x):max(x1,x)]
            region = cv2.blur(region, (15,15))
            region = cv2.GaussianBlur(region, (25,25), cv2.BORDER_DEFAULT)
            tmp[min(y1,y):max(y1,y), min(x1,x):max(x1,x)] = region
            frames.append(tmp)
        position.pop()
        cv2.imshow(window, tmp)

    if event == cv2.EVENT_LBUTTONDOWN:
        click.append(1)
        position.append([x,y])
        frames.append(frames[-1])
        if param[0] == 'eraser':
            mask_tmp = cv2.resize(mask.copy(),(param[2]*2,param[2]*2))
            tmp = frames[-1].copy()
            roix1 = x - param[2]
            roix2 = x + param[2] 
            roiy1 = y - param[2]
            roiy2 = y + param[2] 
            if x < param[2]:
                roix1 = 0
                mask_tmp = mask_tmp[:,param[2]-x:]
            if y < param[2]:
                roiy1 = 0
                mask_tmp = mask_tmp[param[2]-y:, :]
            if x > img.shape[1]-param[2]:
                roix2 = img.shape[1]
                mask_tmp = mask_tmp[:, :mask_tmp.shape[1]-x-param[2]+roix2]
            if y > img.shape[0]-param[2]:
                roiy2 = img.shape[0]
                mask_tmp = mask_tmp[:mask_tmp.shape[0]-y-param[2]+roiy2, :]
            tmp[roiy1:roiy2, roix1:roix2][mask_tmp == 255] = frames[0][roiy1:roiy2, roix1:roix2][mask_tmp == 255]
            frames[-1] = tmp
            cv2.imshow(window, tmp)

    if event == cv2.EVENT_MOUSEMOVE and not len(click):
        tmp = frames[-1].copy()
        if param[2] == -1:
            cv2.circle(tmp, (x, y), fill[0], param[1], -1)
        else:
            cv2.circle(tmp, (x, y), param[2], param[1], -1)
        cv2.imshow(window, tmp)

    if event == cv2.EVENT_MOUSEMOVE and len(click) and param[0] != "eraser":        # drawing
        frames.pop()
        tmp = frames[-1].copy()
        if param[0] == 'rectangle':
            cv2.rectangle(tmp, (position[0][0],position[0][1]), (x, y), param[1] ,param[2])
        if param[0] == 'circle':
            cv2.circle(tmp, (position[0][0],position[0][1]), int(((x-position[0][0])**2+(y-position[0][1])**2)**0.5), param[1], param[2])
        if param[0] == 'line':
            cv2.line(tmp, (position[0][0],position[0][1]), (x, y), param[1] ,param[2])
        if param[0] == 'blur':
            cv2.rectangle(tmp, (position[0][0],position[0][1]), (x, y), param[1] ,param[2])
        if param[0] == 'arrow':
            cv2.arrowedLine(tmp, (position[0][0], position[0][1]), (x, y), param[1], param[2])
        frames.append(tmp)
        cv2.imshow(window, tmp)

    if event == cv2.EVENT_MOUSEMOVE and len(click) and param[0] == "eraser":        #eraser
        mask_tmp = cv2.resize(mask.copy(),(param[2]*2,param[2]*2))
        roix1 = x - param[2]
        roix2 = x + param[2] 
        roiy1 = y - param[2]
        roiy2 = y + param[2] 
        if x < param[2]:
            roix1 = 0
            mask_tmp = mask_tmp[:,param[2]-x:]
        if y < param[2]:
            roiy1 = 0
            mask_tmp = mask_tmp[param[2]-y:, :]
        if x > img.shape[1]-param[2]:
            roix2 = img.shape[1]
            mask_tmp = mask_tmp[:, :mask_tmp.shape[1]-x-param[2]+roix2]
        if y > img.shape[0]-param[2]:
            roiy2 = img.shape[0]
            mask_tmp = mask_tmp[:mask_tmp.shape[0]-y-param[2]+roiy2, :]
        tmp = frames[-1].copy()
        cv2.circle(tmp, (x, y), param[2], param[1], -1)
        cv2.imshow(window, tmp)
        frames[-1][roiy1:roiy2, roix1:roix2][mask_tmp == 255] = frames[0][roiy1:roiy2, roix1:roix2][mask_tmp == 255]


click = []
position = []
fill = []

circle = cv2.imread('/home/noward/Scripts/python/cv/screenshot/circle.png')
mask = cv2.inRange(circle, np.array([1,1,1]), np.array([255,255,255]))

system('import /home/noward/Scripts/python/cv/screenshot/screenshot.png')
img = cv2.imread("/home/noward/Scripts/python/cv/screenshot/screenshot.png", -1)
img = cv2.resize(img, (0,0), fx=0.8, fy=0.8)
frames = [img.copy()]

cv2.namedWindow(window)
cv2.imshow(window,img)

cv2.createTrackbar("RED", window ,0, 255, dummy)
cv2.createTrackbar("GREEN", window ,172, 255, dummy)
cv2.createTrackbar("BLUE", window ,230, 255, dummy)
cv2.createTrackbar("WIDTH", window, 5, 50, dummy)


mode = ''
while True:

    r = cv2.getTrackbarPos("RED",window)
    g = cv2.getTrackbarPos("GREEN",window)
    b = cv2.getTrackbarPos("BLUE",window)
    color = (b,g,r)

    k = cv2.waitKey(1)
    if k & 0xFF == ord('r'):    # rectangle
        mode = 'r' 
    if k & 0xFF == ord('c'):    # circle
        mode = 'c'
    if k & 0xFF == ord('l'):    # line
        mode = 'l'
    if k & 0xFF == ord('e'):    # eraser
        mode = 'e'
    if k & 0xFF == ord('a'):    # arrow
        mode = 'a'
    if k & 0xFF == ord('q'):    # quit
        break 
    if k & 0xFF == ord('b'):    # blur
        mode = 'b'
    if k & 0xFF == ord('y'):    # yank (copy to clipboard, xclip required)
        cv2.imwrite("/home/noward/Scripts/python/cv/screenshot/tmp.png", frames[-1])
        system('/home/noward/Scripts/python/cv/screenshot/copy.sh /home/noward/Scripts/python/cv/screenshot/tmp.png')
    if k & 0xFF == ord('s'):    # save
        cv2.imwrite('/home/noward/Downloads/screenshot/HIMP - {}.png'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), frames[-1])
        break
    if k & 0xFF == ord('z'):    # cancel last move
        if len(frames) > 1:
            frames.pop()
            cv2.imshow(window,frames[-1])
    if k & 0xFF == ord('f'):    # filling mode toggle
        tmp = frames[-1].copy()
        if len(fill):
            fill.pop()
        else:
            fill.append(cv2.getTrackbarPos("WIDTH",window))
    width = cv2.getTrackbarPos("WIDTH",window)
    if len(fill):
        width = -1
        
    if mode == 'r':
        cv2.setMouseCallback(window, onClick, param=['rectangle', color, width])
    if mode == 'c':
        cv2.setMouseCallback(window, onClick, param=['circle', color, width])
    if mode == 'l':
        cv2.setMouseCallback(window, onClick, param=['line', color, cv2.getTrackbarPos("WIDTH",window)])
    if mode == 'a':
        cv2.setMouseCallback(window, onClick, param=['arrow', color, cv2.getTrackbarPos("WIDTH",window)])
    if mode == 'e':
        cv2.setMouseCallback(window, onClick, param=['eraser', (142, 11, 198), cv2.getTrackbarPos("WIDTH", window)])
    if mode == 'b':
        cv2.setMouseCallback(window, onClick, param=['blur', (232,172,0), 5])
    if mode == '':
        cv2.setMouseCallback(window, onClick, param=['', color, cv2.getTrackbarPos("WIDTH",window)])

cv2.destroyAllWindows()

