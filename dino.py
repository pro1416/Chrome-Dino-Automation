import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def takeScreenshot():
    img = ImageGrab.grab().convert('L')
    return img


x1 = 220
x2 = 334
y1 = 374
y2 = 443

def isCollide(data):
    #if day:
    if not data[600,120]== 0:
        # for land objects 
        for i in range(x1,x2):
            for j in range(y1,y2):
                if data[i,j] < 100:
                    hit("up")
                    return
    # for night
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                if data[i,j] > 10:
                    hit("up")
                    return

    #if nothing keep going
    return

def play_game(): 
    time.sleep(3)
    while True:
        image = takeScreenshot()
        image_data = image.load()
        isCollide(image_data)  

if __name__ == "__main__": 
    play_game()
        

        

        

