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
        time.sleep(5)
        dungeonCounter += 1
        if dungeonCounter == 1:
            print("Cleared", dungeonCounter, "run")
        else:
            print("Cleared", dungeonCounter, "runs")

    PetSkill = imagesearch("./Images/PandaSkill.png") 
    if PetSkill[0] != -1:
        pydirectinput.press('6')
        time.sleep(.3)
        pydirectinput.keyDown('w')
        time.sleep(.6)   

        for i in range(3):
            pydirectinput.keyDown('space')
            time.sleep(.4)
            pydirectinput.keyUp('space')
            pydirectinput.leftClick()
            time.sleep(.6)

        pydirectinput.keyUp('w')
        time.sleep(1.5) 
             
    BossBar = imagesearch("./Images/BossBar.png", precision=0.9)
    if BossBar[0] != -1:
        print('boss found')
        pydirectinput.keyDown('w')
        time.sleep(1)
        pydirectinput.keyDown('y')
        time.sleep(4)
        pydirectinput.keyUp('y')
        pydirectinput.keyUp('w')
        time.sleep(3)

        while True:
            SkipMVP = imagesearch("./Images/Skip.png")
            if SkipMVP[0] != -1:
                pydirectinput.press('esc')
                time.sleep(6)
                break
    else:
        print('No boss found. Moving...')
        counter = 0
        while True:
            pydirectinput.keyDown('w')
            pydirectinput.keyDown('space')
            time.sleep(.4)
            pydirectinput.keyUp('space')
            pydirectinput.leftClick()
            pydirectinput.keyUp('w')
            time.sleep(1)
            BossBar = imagesearch("./Images/BossBar.png", precision=0.9)
            if BossBar[0] != -1:
                print('Boss found.')
                counter = 0
                break
            counter +=1

            if counter == 5:
                counter = 0
                pydirectinput.press('esc')
                time.sleep(2)
                TownButton = imagesearch("./Images/TownButton.png")
                if TownButton[0] != -1:
                    pydirectinput.click(TownButton[0],TownButton[1])
                    time.sleep(1)
                    pydirectinput.press('enter')
                    time.sleep(15)
                    pydirectinput.keyDown('s')
                    time.sleep(2)
                    pydirectinput.keyUp('s')
                    ConquestDungeon = imagesearch("./Images/ConquestDungeon.png")
                    if ConquestDungeon[0] != -1:
                        pydirectinput.click(ConquestDungeon[0],ConquestDungeon[1])
                        time.sleep(1)
                        pydirectinput.press('f')
                        time.sleep(10)
                        break
                    else:
                        print('Cannot find dungeon. Exiting...')
                        exit()
                else:
                    print('Cannot head to town. Exiting...')
                    exit()  



