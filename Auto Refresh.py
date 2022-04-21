from pyautogui import *
from ctypes import windll
from random import *

import pyautogui
import time
import keyboard

def img_search(picture, conf=0.90):
    refresh = 0
    position = pyautogui.locateOnScreen(picture, confidence = conf)
    while refresh < 2 and position == None:
        print(picture + ' not found, trying again')
        time.sleep(3)
        position = pyautogui.locateOnScreen(picture)
        refresh += 1
    if position == None:
        print("Something went wrong.")
        windll.user32.MessageBoxW(0, "Something went wrong", "Error", 0)
        results()
    print(picture + ' found, continuing.')
    return position

def results():
    print("Covenant Summons bought:",cont_coven)
    print("Mystic Summons bought:",cont_mystic)
    print("Refreshes Done:",cont_refresh,"// Skystone used:", cont_refresh*3)
    sys.exit("You exited.")

def quit():
    if keyboard.is_pressed('q'):
        results()

# %%Fail-Safes
# # After each pyautogui instruction, wait 0.25 seconds
pyautogui.PAUSE = 0.25
# # If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True

# %%set up
print("Set window now")
time.sleep(3)
# # Get screen res
screensize=pyautogui.size()
# # Move to center of the screen instantly
pyautogui.moveTo(screensize[0]/2, screensize[1]/2, duration=0)
# number of visual inspections done on screen
count=0
# number of coven and mystic bought, and refreshes done
cont_coven, cont_mystic, cont_refresh = 0, 0, 0
# set boolean of coven and mystic purchase (once max per refresh)
coven_bool, mystic_bool = False, False
# maximum number of times to refresh the shop
max_refresh = 2000

# %%
try:
    while keyboard.is_pressed('q') == False and cont_refresh < max_refresh:
        time.sleep(1)

        # The confidence is added due to little variations in the background
        # Search for the price and quantity image of covenant summon
        Coven_pos = pyautogui.locateOnScreen('coven_icon.PNG', confidence=0.90)
        # Search for the price and quantity image of mystic summon
        Mystic_pos = pyautogui.locateOnScreen('mystic_icon.PNG', confidence=0.90)
        
        # Checks for covenant
        if (Coven_pos) != None and coven_bool == False:
            print("Buy Covenant Summons.")
            count = 0
            pyautogui.click(x=Coven_pos[0]+703+randrange(105), y=Coven_pos[1]+70+randrange(55), clicks=2, interval=uniform(0.05,0.1), button='left')
            time.sleep(0.25) # wait for confirm button
            Buy_button_Covenant_pos = pyautogui.locateOnScreen('Buy_button_Covenant.PNG', confidence=0.90)
            try:
                pyautogui.click(x=Buy_button_Covenant_pos[0]+137+randrange(110), y=Buy_button_Covenant_pos[1]+30+randrange(45), clicks=2, interval=uniform(0.05,0.1), button='left')
            except TypeError:
                Buy_button_Covenant_pos = img_search('Buy_button_Covenant.PNG')
                pyautogui.click(x=Buy_button_Covenant_pos[0]+137+randrange(110), y=Buy_button_Covenant_pos[1]+30+randrange(45), clicks=2, interval=uniform(0.05,0.1), button='left')
            cont_coven += 1
            coven_bool = True
            
    # checks for mystic
        if (Mystic_pos) != None and mystic_bool == False:
            print("Buy Mystic Summons.")
            count = 0
            pyautogui.click(x=Mystic_pos[0]+703+randrange(50), y=Mystic_pos[1]+70+randrange(55), clicks=2, interval=uniform(0.05,0.1), button='left')
            time.sleep(0.25)# wait for confirm button
            Buy_button_Mystic_pos = pyautogui.locateOnScreen('Buy_button_Mystic.PNG', confidence=0.90)
            try:
                pyautogui.click(x=Buy_button_Mystic_pos[0]+137+randrange(110), y=Buy_button_Mystic_pos[1]+30+randrange(45), clicks=2, interval=uniform(0.05,0.1), button='left')
            
            except TypeError:
                Buy_button_Mystic_pos = img_search('Buy_button_Mystic.PNG')
                pyautogui.click(x=Buy_button_Mystic_pos[0]+137+randrange(110), y=Buy_button_Mystic_pos[1]+30+randrange(45), clicks=2, interval=uniform(0.05,0.1), button='left')
            cont_mystic += 1
            mystic_bool = True
            
        else:
            time.sleep(0.05)
            # print("No Mystic summons to buy.")

        # Center cursor and then scroll down
        pyautogui.scroll(-2,screensize[0]/2, screensize[1]/2)
        count += 1
        time.sleep(0.25)
            
    # Double check in case of lag don't enable unless you're lagging
        #  if count==2 :
        #      pyautogui.moveTo(screensize[0]/2, screensize[1]/2, duration=0)
        #      # Drag upward 300 pixels in 0.2 seconds
        #      pyautogui.dragTo(screensize[0]/2, screensize[1]/2-300, duration=0.2)
        #      time.sleep(0.5)
    # Finally refreshes
        while count>=2 :
            refresh_pos = pyautogui.locateOnScreen('refresh_button.PNG', confidence = 0.90)
            try:
                pyautogui.click(x=refresh_pos[0]+260+randrange(140), y=refresh_pos[1]+15+randrange(60), clicks=2, interval=uniform(0.05,0.1), button='left')
            except:
                refresh_pos = img_search('refresh_button.PNG')
                pyautogui.click(x=refresh_pos[0]+260+randrange(140), y=refresh_pos[1]+15+randrange(60), clicks=2, interval=uniform(0.05,0.1), button='left')
            time.sleep(0.35)# wait for confirm to appear
            Confirm_pos = pyautogui.locateOnScreen('confirm button.PNG', confidence=0.90)
            try:
                pyautogui.click(x=Confirm_pos[0]+35+randrange(55), y=Confirm_pos[1]+20+randrange(35), clicks=2, interval=uniform(0.05,0.1), button='left')
            
            except TypeError:
                Confirm_pos = img_search('confirm button.PNG')
                pyautogui.click(x=Confirm_pos[0]+35+randrange(55), y=Confirm_pos[1]+20+randrange(35), clicks=2, interval=uniform(0.05,0.1), button='left')
            count = 0
            coven_bool, mystic_bool = False, False
            time.sleep(0.1)
            print('Refresh #: ', cont_refresh)
            cont_refresh += 1
except pyautogui.FailSafeException:
    print('Failsafe executed. Program ended.')
    windll.user32.MessageBoxW(0, "Failsafe invoked", "Done", 0)
# %%Outside of the while loop
print("Program exited successfully.")
windll.user32.MessageBoxW(0, "Program exited successfully", "Done", 0)
results()