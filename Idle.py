#OH BOY HOPE YOU LIKE SPAGHETTI

import subprocess
import time
import psutil

#Hippity Hopity
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
#Your code is now my property (https://gist.github.com/Sanix-Darker/8cbed2ff6f8eb108ce2c8c51acd2aa5a) 
    
y=0 #while true didnt work 
while y == 0:
    x=subprocess.check_output(['xprintidle'])
    z=float(x) #if statements require float to work
    if z >= 300000: #You're going to wait five minutes and you are going to like it! (unless you change the value-my only weakness)
        if checkIfProcessRunning('xmr-stak-rx'):
            time.sleep(1)
        else :
            subprocess.Popen(['./xmr-stak-rx --noTest'])
            print("\n" + 'Started miner' + "\n")
            time.sleep(1)
    else :
        if checkIfProcessRunning('xmr-stak-rx'):
            subprocess.run(['killall xmr-stak-rx'], shell=True) #I just wasted two hours of my time looking for workarounds for this line, just to find out I only needed to add ", shell=True". (╯°□°)╯︵ ┻━┻
            print("\n" + 'Killed miner' + "\n")
            time.sleep(1)
        else:
            time.sleep(1)
