from pyautogui import *
import pyautogui
import time
import keyboard
# import random

def img_search(picture, conf=0.90):
    refresh = 0
    try:
        position = pyautogui.locateAllOnScreen(picture, confidence = conf)
    except TypeError:
        while refresh < 2 and position is None:
            print(picture + ' not found, trying again')
            time.sleep(3)
            position = pyautogui.locateAllOnScreen(picture)
    return position

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
while keyboard.is_pressed('q') == False and cont_refresh < max_refresh:
    time.sleep(0.25)

    # The confidence is added due to little variations in the background
    # Search for the refresh button
    refresh_pos = img_search('refresh_button.PNG')
    # Search for the price and quantity image of covenant summon
    Coven_pos = img_search('coven_icon.PNG')
    # Search for the price and quantity image of mystic summon
    Mystic_pos = img_search('mystic_icon.PNG')
    
    # Checks for covenant
    if (Coven_pos) != None and coven_bool == False:
        print("Buy Covenant Summons.")
        count=0
        Coven_point=pyautogui.center(Coven_pos)
        pyautogui.click(x=Coven_point[0]+800, y=Coven_point[1]+30, button='left')
        time.sleep(0.25) # wait for confirm button
        Buy_button_Covenant_pos=img_search('Buy_button_Covenant.PNG')
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        cont_coven+=1
        coven_bool = True
        
# checks for mystic
    if (Mystic_pos) != None and mystic_bool == False:
        print("Buy Mystic Summons.")
        count=0
        Mystic_point=pyautogui.center(Mystic_pos)
        pyautogui.click(x=Mystic_point[0]+800, y=Mystic_point[1]+30, clicks=2, interval=0.05, button='left')
        time.sleep(0.25)# wait for confirm button
        Buy_button_Mystic_pos=img_search('Buy_button_Mystic.PNG')
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        cont_mystic+=1
        mystic_bool = True
        
    else:
        time.sleep(0.05)
        # print("No Mystic summons to buy.")

    # Center cursor and then scroll down
    pyautogui.scroll(-2,screensize[0]/2, screensize[1]/2)
    count += 1
    time.sleep(0.1)
        
# Double check in case of lag don't enable unless you're lagging
    #  if count==2 :
    #      pyautogui.moveTo(screensize[0]/2, screensize[1]/2, duration=0)
    #      # Drag upward 300 pixels in 0.2 seconds
    #      pyautogui.dragTo(screensize[0]/2, screensize[1]/2-300, duration=0.2)
    #      time.sleep(0.5)
# Finally refreshes
    while count>=2 :
        refresh_point=pyautogui.center(refresh_pos)
        pyautogui.click(x=refresh_point[0], y=refresh_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(0.35)# wait for confirm to appear
        Confirm_pos=img_search('confirm button.PNG')
        Confirm_point=pyautogui.center(Confirm_pos)
        pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
        count=0
        coven_bool, mystic_bool = False, False
        time.sleep(0.1)
        cont_refresh+=1
        
# %%Outside of the while loop
print("You exited successfully")
print("Covenant Summons bought:",cont_coven)
print("Mystic Summons bought:",cont_mystic)
print("Refreshes Done:",cont_refresh,"// Skystone used:", cont_refresh*3)
