import subprocess
import time
import psutil

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
    
y=0 #while true didnt work 
while y == 0:
    x=subprocess.check_output(['xprintidle'])
    z=float(x) #if statements require float to work
    if z >= 300000: 
        if checkIfProcessRunning('xmr-stak-rx'):
            time.sleep(1)
        else :
            subprocess.Popen(['./xmr-stak-rx --noTest'])
            print("\n" + 'Started miner' + "\n")
            time.sleep(1)
    else :
        if checkIfProcessRunning('xmr-stak-rx'):
            subprocess.run(['killall xmr-stak-rx'], shell=True)
            print("\n" + 'Killed miner' + "\n")
            time.sleep(1)
        else:
            time.sleep(1)
