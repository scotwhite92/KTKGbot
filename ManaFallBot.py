from python_imagesearch.imagesearch import imagesearch
import pydirectinput
import time



print("Starting in 3 seconds. Switch to KTKG!")
time.sleep(3)

dungeonCounter = 0

while True:
    RestartStage = imagesearch("./Images/RestartStage.png")
    if RestartStage[0] != -1:
        pydirectinput.press('f1')
        time.sleep(.3)
        pydirectinput.press('f4')
        time.sleep(1)
        dungeonCounter += 1
        if dungeonCounter == 1:
            print("Cleared", dungeonCounter, "run")
        else:
            print("Cleared", dungeonCounter, "runs")

    PetSkill = imagesearch("./Images/PandaSkill.png") 
    if PetSkill[0] != -1:
        pydirectinput.press('6')
        pydirectinput.press('6')
        time.sleep(.3)
        pydirectinput.press('f3')
        time.sleep(.1)
        pydirectinput.keyDown('z')
        time.sleep(1)
        pydirectinput.press('v')
        pydirectinput.keyUp('z')
        time.sleep(.5)
        pydirectinput.press('3')
        time.sleep(1)   

    BlackScreen = imagesearch("./Images/BlackScreen.png")
    if BlackScreen[0] != -1:
        time.sleep(.5)
    
    LoadingScreen = imagesearch("./Images/LoadingScreen.png")
    if LoadingScreen[0] != -1:
        time.sleep(.5)
             
    BossBar = imagesearch("./Images/BossBar.png", precision=0.9)
    if BossBar[0] != -1:
        #print('boss found')
        pydirectinput.press('z')
        time.sleep(.5)
        pydirectinput.press('esc')
        time.sleep(.2)
        pydirectinput.keyUp('w')
        pydirectinput.press('f2')
        time.sleep(.3)
        pydirectinput.press('y')
        time.sleep(2)
        counter = 0
        while True:
            
            SkipMVP = imagesearch("./Images/Skip.png")
            if SkipMVP[0] != -1:
                pydirectinput.press('esc')
                time.sleep(1)
                break
            else:
                counter +=1
                time.sleep(1)

                if counter == 5:
                    counter = 0
                    pydirectinput.press('enter')
                    time.sleep(.25)
                    pydirectinput.press('enter')
                    time.sleep(.25)
                    pydirectinput.press('enter')
                    time.sleep(.25)
                    pydirectinput.press('esc')
                    time.sleep(.5)
                    pydirectinput.press('esc')
                    time.sleep(2)
                    TownButton = imagesearch("./Images/EscMenu.png")
                    if TownButton[0] != -1:
                        pydirectinput.click(1413,447)
                        time.sleep(1)
                        pydirectinput.press('enter')
                        time.sleep(15)
                        pydirectinput.press('f3')
                        pydirectinput.keyDown('s')
                        time.sleep(2)
                        pydirectinput.keyUp('s')
                        ConquestDungeon = imagesearch("./Images/SunShrineDungeon.png")
                        if ConquestDungeon[0] != -1:
                            pydirectinput.click(958,620)
                            time.sleep(1)
                            pydirectinput.press('f')
                            time.sleep(1)
                            break
                        else:
                            print('Cannot find dungeon. Exiting...')
                            exit()
                    else:
                        print('Cannot head to town. Exiting...')
                        exit()  
