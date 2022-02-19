import tkinter as tk
from tkinter import ttk
import subprocess, psutil, time, threading 

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
def Idle():
	button.state(['disabled'])
	#button2.state(['!disabled'])
	while True:
                    u=subprocess.check_output(['xprintidle'])
                    z=float(u) #if statements require float to work
                    if z >= 300000: 
                        if checkIfProcessRunning('xmr-stak-rx'):
                            time.sleep(1)
                        else :
                            subprocess.Popen(['./xmr-stak-rx'])
                            print("\n" + 'Started miner' + "\n")
                            time.sleep(1)
                    else :
                        if checkIfProcessRunning('xmr-stak-rx'):
                            subprocess.run(['killall xmr-stak-rx'], shell=True) 
                            print("\n" + 'Killed miner' + "\n")
                            time.sleep(1)
                        else:
                            time.sleep(1)
                    
s= threading.Thread(target=Idle, args=())

def jimmy():
	s.start()
	
#def timmy():
	#button2.state(['disabled'])
	#button.state(['!disabled'])
	#The original plan was to have a start and stop button but until I figure out how to kill a thread that isnt going to happen

root = tk.Tk()
root.geometry('150x50')
root.resizable(False, False)
root.title('Idle Miner')

button = ttk.Button(root,
 text='Start Idle Miner', 
 command= lambda: jimmy()
)
button.place(x=10, y=10)

#button2 = ttk.Button(root,
# text='Stop Idle Miner', 
# command= lambda: timmy()
#)
#button2.place(x=150, y=10)
#button2.state(['disabled'])
#The original plan was to have a start and stop button but until I figure out how to kill a thread that isnt going to happen


root.mainloop()
