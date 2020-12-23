import cv2
import glob
import win32api
#import numpy as np
from ctypes import windll



abc = False
images = glob.glob('./before/*.png')
imageIndex = 0
img = ''
pointSize = 15
wname = 'Bluring'
cv2.namedWindow(wname)
hicon = ""

def draw_eraser(event, x, y, flags, param):
    global abc
    global img

    if event == cv2.EVENT_LBUTTONDOWN:
        abc = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if (abc == True):
            blur = img[y:y + pointSize, x:x + pointSize]
            blur = cv2.GaussianBlur(blur, (23, 23), 50)
            img[y:y + blur.shape[0], x:x + blur.shape[1]] = blur
    else:
        abc = False
'''
def hangulFilePathImageRead ( filePath ) :
    stream = open( filePath.encode("utf-8") , "rb")
    bytes = bytearray(stream.read())
    numpyArray = np.asarray(bytes, dtype=np.uint8)

    return cv2.imdecode(numpyArray , cv2.IMREAD_UNCHANGED)
'''


def createCursor():
    global hicon
    CreateIconFromResourceEx = windll.user32.CreateIconFromResourceEx
    size_x, size_y = pointSize, pointSize
    LR_DEFAULTCOLOR = 0

    with open("lpoint.png", "rb") as f:
        png = f.read()
    hicon = CreateIconFromResourceEx(png, len(png), 1, 0x30000, size_x, size_y, LR_DEFAULTCOLOR)

    print("point size : "+str(pointSize))

def showCursor():
    win32api.SetCursor(hicon)  # change cursor

createCursor()


if len(images) != 0:
    img = cv2.imread(images[imageIndex])
    cv2.setMouseCallback(wname, draw_eraser)
    print(images[imageIndex])


while True:
    showCursor()
    cv2.imshow(wname, img)

    c = cv2.waitKey(1)

    if c == ord('p'):
        break
    elif c == ord('n'):
        #기존 이미지 저장
        imageName = images[imageIndex].split('\\')
        cv2.imwrite('./after/'+imageName[len(imageName)-1],img)

        #새 이미지 불러오기
        imageIndex = imageIndex + 1
        if imageIndex >= len(images):
            break
        img = cv2.imread(images[imageIndex])
        #img = hangulFilePathImageRead(images[imageIndex])
        cv2.imshow(wname, img)
        #cv2.imshow(wname,"23_160577294815101520044-복사본.jpg")
        print(images[imageIndex])


    elif c == 44:
        if pointSize > 5:
            pointSize = pointSize-1
            createCursor()

    elif c == 46:
        if pointSize < 100:
            pointSize = pointSize+1
            createCursor()


cv2.destroyAllWindows()