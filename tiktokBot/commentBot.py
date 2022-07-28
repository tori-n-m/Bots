import pyautogui
import time

#Uses iPhone 6/7/8. Modify dimensions depending on what computer is being used

while True:
    
    for i in range(100):

        #pauses the video
        pyautogui.click(535, 615)
        time.sleep(2)

        #opens the comment section
        pyautogui.click(713, 699)
        time.sleep(4)

        #clicks input box
        pyautogui.click(445, 957)
        time.sleep(2)

        #writes comment
        if i <= 10:
            pyautogui.write("Follow for follow", interval=0.2)
            time.sleep(2)

        if i <= 20 and i >= 11:
            pyautogui.write("Follow for follow!", interval=0.2)
            time.sleep(2)

        if i <= 30 and i >= 21:
            pyautogui.write("You follow me, I'll follow you", interval=0.2)
            time.sleep(2)

        if i <= 40 and i >= 31:
            pyautogui.write("If you follow me, I'll follow you", interval=0.2)
            time.sleep(2)

        if i <= 50 and i >= 41:
            pyautogui.write("If you follow me, I'll follow you!", interval=0.2)
            time.sleep(2)

        if i <= 60 and i >= 51:
            pyautogui.write("You follow me, I'll follow you!", interval=0.2)
            time.sleep(2)

        if i <= 70 and i >= 61:
            pyautogui.write("You follow me, I'll follow you!!", interval=0.2)
            time.sleep(2)

        if i <= 80 and i >= 71:
            pyautogui.write("If you follow me, I'll follow you!!", interval=0.2)
            time.sleep(2)

        if i <= 90 and i >= 81:
            pyautogui.write("If you follow me, I'll follow you!!!", interval=0.2)
            time.sleep(2)

        if i <= 100 and i >= 91:
            pyautogui.write("You follow me, I'll follow you!!!", interval=0.2)
            time.sleep(2)

        #sends comment
        pyautogui.click(721, 955)
        time.sleep(2)

        #closes the comment section
        pyautogui.click(722, 478)
        time.sleep(2)

        #goes to next video
        pyautogui.moveTo(530, 912)
        pyautogui.dragTo(541,284, 1)

