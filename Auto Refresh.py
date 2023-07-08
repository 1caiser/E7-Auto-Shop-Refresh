from pyautogui import *
from random import *
from tkinter import messagebox

import pyautogui
import keyboard
import time
import sys

def break_on_key():
    if keyboard.is_pressed('q'):
        print('Manually exiting')
        results()

def img_search(picture, conf=0.90, maxrefresh=1):
    refresh = 0
    position = pyautogui.locateOnScreen(picture, confidence = conf)
    
    if maxrefresh > 0:
        while position == None:
            print("'" + picture + '" not found, trying again')
            time.sleep(3)
            position = pyautogui.locateOnScreen(picture, confidence = conf)
            refresh += 1
            if refresh > (maxrefresh):
                print('Something went wrong: \"' + picture + '\" not found.')
                messagebox.showinfo("Error", "\"" + picture + "\" not found")
                results()
        if refresh > 0:
            print(picture + ' found, continuing.')
    return position

def dclick_with_random(position, d_x=0, d_y=0, r_x=0, r_y=0):
    # should rewrite as (position, d_x=0, d_y=0, r_x=0, r_y=0, numclicks=1):
    # done
    pyautogui.doubleClick(x=position[0]+d_x+randrange(r_x), y=position[1]+d_y+randrange(r_y), interval=uniform(0.1,0.3))

def results():
    print("Covenant Summons bought:",cont_coven)
    print("Mystic Summons bought:",cont_mystic)
    print("Refreshes Done:",cont_refresh,"// Skystone used:", cont_refresh*3)
    messagebox.showinfo("Results", "Covenant Summons bought: "+ str(cont_coven) + 
                        "\nMystic Summons bought: " + str(cont_mystic) +
                        "\nRefreshes done: "+ str(cont_refresh))
    sys.exit(0)


# %%Fail-Safes
# # After each pyautogui instruction, wait 0.25 seconds
pyautogui.PAUSE = uniform(0.2,0.35)
# # If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True

# %%set up
# # Get screen res
screensize=pyautogui.size()
# # Move to center of the screen 
pyautogui.moveTo(screensize[0]/2, screensize[1]/2, duration=0)
# number of visual inspections done on screen
count=0
# number of coven and mystic bought, and refreshes done
cont_coven, cont_mystic, cont_refresh = 0, 0, 0
# set boolean of coven and mystic purchase (once max per refresh)
coven_bool, mystic_bool = False, False
# maximum number of skystone used to refresh the shop
max_skystone = 9000
# program ready to begin
print("Set window now")
time.sleep(3)

# %%
try:
    while cont_refresh < (max_skystone/3):
        break_on_key()
        time.sleep(1)

        # The confidence is added due to little variations in the background
        # Search for the price and quantity image of covenant summon
        Coven_pos = img_search('coven_icon.png', maxrefresh=0)
        # Search for the price and quantity image of mystic summon
        Mystic_pos = img_search('mystic_icon.png', maxrefresh=0)
        
        # Checks for covenant
        if Coven_pos != None and coven_bool == False:
            print("Buy Covenant Summons.")
            count = 0
            dclick_with_random(Coven_pos, 703, 70, 50, 55)
            # TODO: any d_x, etc arguments need to be replaced with screensize ratios
            Buy_button_Covenant_pos = img_search('Buy_button_Covenant.png')
            try:
                dclick_with_random(Buy_button_Covenant_pos, 137, 30, 110, 45)
            except TypeError:
                # running ras/lag?
                time.sleep(3)
                dclick_with_random(Coven_pos, 703, 70, 105, 55)
                Buy_button_Covenant_pos = img_search('Buy_button_Covenant.png',3)
                dclick_with_random(Buy_button_Covenant_pos, 137, 30, 110, 45)
            cont_coven += 1
            coven_bool = True
            
        # checks for mystic
        if (Mystic_pos) != None and mystic_bool == False:
            print("Buy Mystic Summons.")
            count = 0
            dclick_with_random(Mystic_pos, 703, 70, 50, 55)
            Buy_button_Mystic_pos = img_search('Buy_button_Mystic.png')
            try:
                dclick_with_random(Buy_button_Mystic_pos, 137, 30, 110, 45)
            except TypeError:
                # running ras/lag?
                time.sleep(3)
                dclick_with_random(Mystic_pos, 703, 70, 50, 55)
                Buy_button_Mystic_pos = img_search('Buy_button_Mystic.png',3)
                dclick_with_random(Buy_button_Mystic_pos, 137, 30, 110, 45)
            cont_mystic += 1
            mystic_bool = True

        # Scroll down
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
        
        break_on_key()
        while count >= 2:
            refresh_pos = img_search('refresh_button.png')
            dclick_with_random(refresh_pos,260,15,140,60)
            time.sleep(uniform(0.5,0.75))

            """Confirm_pos = img_search('confirm_button.png')
            try:
                dclick_with_random(Confirm_pos,35,20,55,35)
            except:
                # comfirm button not respond?
                dclick_with_random(refresh_pos,260,15,140,60)
                Confirm_pos = img_search('confirm_button.png', 3)"""
            #check that confirm button got pressed
            deadlock = 0
            Confirm_pos = img_search('confirm_button.png', maxrefresh=0)
            while Confirm_pos != None:
                # if not None, click button and check again
                dclick_with_random(Confirm_pos,35,20,55,35)
                Confirm_pos = img_search('confirm_button.png', maxrefresh=0)
                deadlock += 1
                if Confirm_pos == None:
                    break
                if deadlock > 3:
                    print("Interrupted, or unresponsive.")
                    messagebox.showinfo("Error","Interrupted, or unresponsive.")
                    results()

            count = 0
            coven_bool, mystic_bool = False, False
            time.sleep(0.1)
            print('Refresh #:', cont_refresh+1)
            cont_refresh += 1
except pyautogui.FailSafeException:
    print('Failsafe invoked. Program ended.')
    results()
    

# %%Outside of the while loop
print("Program exited successfully.")
results()