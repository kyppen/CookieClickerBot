from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(2)


def click(x, y):  # Function for making the mouse click
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def upgrade():  # Attempts to upgrade
    x = 0
    click_time = 0.02
    if keyboard.is_pressed("q") == False:
        while x < 1:
            click(1631, 260)
            time.sleep(click_time)
            click(1691, 260)
            time.sleep(click_time)
            click(1751, 260)
            time.sleep(click_time)
            click(1783, 880)
            time.sleep(click_time)
            click(1788, 825)
            time.sleep(click_time)
            click(1787, 756)
            time.sleep(click_time)
            click(1789, 677)
            time.sleep(click_time)
            click(1789, 601)
            time.sleep(click_time)
            click(1796, 546)
            time.sleep(click_time)
            click(1803, 490)
            time.sleep(click_time)
            click(1821, 422)
            time.sleep(click_time)
            click(1800, 358)
            time.sleep(click_time)
            click(1751, 260)
            x = x + 1


def click_cookie():  # Clicks the cookie
    x = 0
    if keyboard.is_pressed("q") == False:
        while x < 100:
            x_cookie = 294
            y_cookie = 486
            time.sleep(0.02)
            click(x_cookie, y_cookie)
            x = x + 1


def close_achievements():
    if keyboard.is_pressed("q") == False:
        try:
            x, y = pyautogui.locateCenterOnScreen("exit.PNG", confidence=0.9, grayscale=True)
            click(x, y)
       	    time.sleep(0.5)
        except:
            print("nothing to close")

def goldencookie():
    if keyboard.is_pressed("q") == False:
        try:
            x, y = pyautogui.locateCenterOnScreen("attempt.PNG", confidence=0.4, grayscale=True)
            click(x, y)
        except:
            print("looking for cookies part 1")
        

def goldencookie2():
    if keyboard.is_pressed("q") == False:
        try:
            x, y = pyautogui.locateCenterOnScreen("goldencookie.PNG", confidence=0.4, grayscale=True)
            click(x,y)
        except:
            print("looking for cookies part 2")

def main_loop():
    if keyboard.is_pressed("q") == False:
        x = 0
        time_XD = 0.05
        while x < 100:
            if keyboard.is_pressed("o") == True:
                sys.exit()
            time.sleep(time_XD)
            print("Starting to upgrade")
            upgrade()
            time.sleep(time_XD)
            goldencookie()
            goldencookie2()
            print("Farming cookies now")
            click_cookie()
            time.sleep(time_XD)
            print("Closing the achievements")
            close_achievements()
            time.sleep(time_XD)
            print("Looking for golden cookies")
            goldencookie()
            goldencookie2()

def restart():
    if keyboard.is_pressed("q") == False:
        x, y = pyautogui.locateCenterOnScreen("options.PNG", confidence=0.9, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen("Wipe.PNG", confidence=0.9, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen("yes.PNG", confidence=0.9, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen("Do_it.PNG", confidence=0.9, grayscale=True)
        click(x,y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen("options.PNG", confidence=0.9, grayscale=True)
        click(x,y)
        time.sleep(0.5)


def restart_and_start():   
    restart()
    main_loop()

x = input("What to do? [Start] [Reset] [Reset and Start] ")

if x == "Start":
    main_loop()

if x == "Reset":
    restart()

if x == "Reset and Start":
    restart_and_start()
