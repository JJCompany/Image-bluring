import cv2
import glob
import win32api
import os.path

from ctypes import windll

indexFileName = 'index.txt'
is_bluring = False
is_change = False #이미지 블러 유무 체크

indexFile = open(indexFileName,'r')
images = glob.glob('./before/*.png')
#afterImages = glob.glob('./after/*.png')
afterImages = indexFile.readline()
if afterImages == 'e':#끝났었을 경우 다시 0으로 초기화
    afterImages = 0

imageIndex = 0
img = ''
pointSize = 15
wname = 'Bluring'
cv2.namedWindow(wname)
hicon = ""
#print(images)

def saveIndex(index):
    global indexFileName
    indexFile = open(indexFileName,'w')
    indexFile.write(str(index))
    indexFile.close()


def draw_eraser(event, x, y, flags, param):
    global is_bluring, is_change, img

    if event == cv2.EVENT_LBUTTONDOWN:
        is_bluring = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if (is_bluring == True):
            blur = img[y:y + pointSize, x:x + pointSize]
            blur = cv2.GaussianBlur(blur, (3,3), 0)
            img[y:y + blur.shape[0], x:x + blur.shape[1]] = blur
            is_change = True
    else:
        is_bluring = False

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

def showImage(index):
    global wname,img, is_change

    is_change = False
    img = cv2.imread(images[index])
    cv2.imshow(wname, img)
    print(images[imageIndex])

createCursor()

if len(images) != 0 and afterImages != len(images):
    cv2.setMouseCallback(wname, draw_eraser)

    imageIndex = int(afterImages)
    #if len(afterImages) != 0:
        #imageIndex = len(afterImages)

    saveIndex(imageIndex)
    showImage(imageIndex)#최초 이미지 로딩


    while True:
        showCursor()
        cv2.imshow(wname, img)

        c = cv2.waitKey(1)

        if c == ord('p'):#프로그램 중지
            break
        elif c == ord('1'):#이미지 저장 + 다음 이미지 불러옫기
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./1/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('2'):
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./2/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('3'):
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./3/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('4'):
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./4/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('5'):
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./5/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('6'):
            #기존 이미지 저장
            imageName = images[imageIndex].split('\\')
            imageName = imageName[len(imageName)-1]

            if is_change:
                imageName = imageName.replace("_N_","_E_")#실제 파일명 뽑기

            cv2.imwrite('./6/'+imageName,img)

            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break

            saveIndex(imageIndex)
            showImage(imageIndex)
        elif c == ord('b'):#이전 이미지 불러오기
            imageIndex = imageIndex -1
            if imageIndex < 0:
                saveIndex(0)
                break
            else :
                saveIndex(imageIndex)
                showImage(imageIndex)
                delName = images[imageIndex].split('\\')
                delName = delName[len(delName)-1]
                delName2 = delName.replace("_N_", "_E_")#다른 파일명 뽑기

                if os.path.isfile('./1/'+delName):#파일이 있는 경우
                    os.remove('./1/'+delName)
                    print('./1/'+delName)
                elif os.path.isfile('./1/'+delName2):
                    os.remove('./1/'+delName2)
                    print('./1/'+delName2)
                elif os.path.isfile('./2/'+delName):
                    os.remove('./2/'+delName)
                    print('./2/'+delName)
                elif os.path.isfile('./2/' + delName2):
                    os.remove('./2/' + delName2)
                    print('./2/' + delName2)
                elif os.path.isfile('./3/' + delName):
                    os.remove('./3/' + delName)
                    print('./3/' + delName)
                elif os.path.isfile('./3/' + delName2):
                    os.remove('./3/' + delName2)
                    print('./3/' + delName2)
                elif os.path.isfile('./4/' + delName):
                    os.remove('./4/' + delName)
                    print('./4/' + delName)
                elif os.path.isfile('./4/' + delName2):
                    os.remove('./4/' + delName2)
                    print('./4/' + delName2)
                elif os.path.isfile('./5/' + delName):
                    os.remove('./5/' + delName)
                    print('./5/' + delName)
                elif os.path.isfile('./5/' + delName2):
                    os.remove('./5/' + delName2)
                    print('./5/' + delName2)
                elif os.path.isfile('./6/' + delName):
                    os.remove('./6/' + delName)
                    print('./6/' + delName)
                elif os.path.isfile('./6/' + delName2):
                    os.remove('./6/' + delName2)
                    print('./6/' + delName2)
                        
        elif c == ord('j'):#다음 이미지 불러오기 + 이미지 저장 없음
            #새 이미지 불러오기
            imageIndex = imageIndex + 1
            if imageIndex >= len(images):
                saveIndex('e')
                break
            saveIndex(imageIndex)
            showImage(imageIndex)
            
        elif c == ord('r'):#이미지 리로드
            showImage(imageIndex)
            
        elif c == 44:#포인터 사이즈 다운
            if pointSize > 5:
                pointSize = pointSize-1
                createCursor()

        elif c == 46:#포인터 사이즈 업
            if pointSize < 100:
                pointSize = pointSize+1
                createCursor()

cv2.destroyAllWindows()
