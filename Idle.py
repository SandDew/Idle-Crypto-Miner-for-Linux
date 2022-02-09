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
    if z >= 3000:
        print('Idle')
        time.sleep(1)
    else :
        print('Not Idle')
        time.sleep(1)


#  x=subprocess.run(['xprintidle'])
#    print("X is next")
 #  print(x)
 #   time.sleep(1)
