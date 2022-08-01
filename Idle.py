import tkinter as tk
from tkinter import ttk
import subprocess, psutil, time, threading

subprocess.run(['killall python3 -o 1s'], shell=True) #Kills all past instances of the miner (just in case) 

#checkIfProcessRunning is taken from https://gist.github.com/Sanix-Darker/8cbed2ff6f8eb108ce2c8c51acd2aa5a
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
    
def IsXmrStakRunning():
	if checkIfProcessRunning('xmr-stak-rx'):
		return True
	else:
		return False		

def IsXmrigRunning():
	if checkIfProcessRunning('xmrig'):
		return True
	else:
		return False	
		
def StartXmrStakRx():
	subprocess.Popen(['./xmr-stak-rx'])
	
def StartXmrig():
	subprocess.Popen(['./xmrrig'])
    
def Idle():
	while True:
		Variable=open("Variable.txt", "r") #Variable = start button
		Has_The_Button_Been_Pressed=Variable.read() 
		if Has_The_Button_Been_Pressed=='True': #(Turns true when stop button is pressed)
			if checkIfProcessRunning('xmr-stak-rx') or checkIfProcessRunning('xmrig'):
                            subprocess.run(['killall xmr-stak-rx'], shell=True) 
                            subprocess.run(['killall xmrig'], shell=True) 
                            print('Made sure the miner was dead')
                            #This code makes sure the miners have been stopped, they should already be dead. But it doesnt hurt to be redundant  
                            time.sleep(1)
			else :
				time.sleep(1) #If the button happens to be on "start idle miner" however, wait one second
		else:
                    Variable2=open("Variable2.txt","r") #Variable 2 is the number of milliseconds it takes to enter an idle state 
                    Time_Till_Idle=Variable2.read()
                    TTI_but_In_Float=float(Time_Till_Idle)
                    Amount_Of_Time_Idle=subprocess.check_output(['xprintidle'])
                    AOTI_but_In_Float=float(Amount_Of_Time_Idle) #Requires float to work
                    if AOTI_but_In_Float >= TTI_but_In_Float: 
                        if IsXmrStakRunning() and IsXmrigRunning():
                            time.sleep(1)
                        else :
                        	if IsXmrStakRunning():
                        		time.sleep(1)
                        	else:
                        		XmrStakThread = threading.Thread(target = StartXmrStakRx, args=())
                        		XmrStakThread.start()
                        	if IsXmrigRunning():
                        		time.sleep(1)
                        	else:
                        		XmrigThread = threading.Thread(target = StartXmrig, args=())
                        		XmrigThread.start()
                        	print("\n" + 'Started miner' + "\n")
                        	time.sleep(1)

                    else :
                        if IsXmrStakRunning() or IsXmrigRunning():
                            subprocess.run(['killall xmr-stak-rx'], shell=True)
                            subprocess.run(['killall xmrig'], shell=True)
                            print("\n" + 'Killed miner' + "\n")
                            time.sleep(1)
                        else:
                            time.sleep(1)
def warning():
	warn=tk.Tk()
	warn.geometry('300x25')
	warn.resizable(False,False)
	warn.title('WARNING')
	
	the_warning= tk.Label(warn, text='The input needs to be a number')
	the_warning.pack()

def jimmy(): #rewrite jimmy, timmy, and clide to have more understandable variable names
	#I wasnt able to use x=1 or x=0 for the break flag. This was the soulution I came up with, im aware that writing to a file is not very efficient. 
	Variable=open("Variable.txt", "w")
	Variable.truncate()
	Variable.write("False")
	Variable.close()
	button.state(['disabled'])
	button2.state(['!disabled'])
	
def timmy():
	Variable=open("Variable.txt", "w")
	Variable.truncate()
	Variable.write("True")
	Variable.close()
	button2.state(['disabled'])
	button.state(['!disabled'])
	
def clide():
	side=box.get()
	try:
		int(side)
		showwarn=False
	except ValueError:
		showwarn=True
	if showwarn == True:
		warning()
	else:
		Variable2=open('Variable2.txt', "w")
		Variable2.truncate()
		Variable2.write(side)
		Variable2.close
		
def Keep_Window_Closed_On_Restart():
	Window_Closed_Flag=open("ClosedWindow.txt", 'w')
	Window_Closed_Flag.truncate()
	Window_Closed_Flag.write("True")
	Window_Closed_Flag.close()
	DontShowWindow.state(['disabled'])
	
def Is_Closed_True():
	flag=open("ClosedWindow.txt", "r")
	flag2=flag.read()
	if flag2 == "True":
		return True
	else:
		return False
	

IdleThread = threading.Thread(target=Idle, args=())
IdleThread.start()

root = tk.Tk()
root.geometry('455x75')
root.resizable(False, False)
root.title('Idle Miner')

DontShowWindow= ttk.Button(root, text = "Dont show window", command= lambda: Keep_Window_Closed_On_Restart())
DontShowWindow.grid(row=0, column=2, padx=5, pady=5)

button = ttk.Button(root,
 text='Start Idle Miner', 
command= lambda: jimmy()
)
button.grid(row=0, column=0, padx=10, pady=5)

button2 = ttk.Button(root,
 text='Stop Idle Miner', 
 command= lambda: timmy()
)
button2.grid(row=0,column=1,padx=5,pady=5)
button2.state(['disabled'])

txt= tk.Label(root, text="Time to idle (ms):")
txt.grid(row=2,column=0,padx=5, pady=5)

Variable2 = open("Variable2.txt", "r") #I dont know how to only delete one line of a file, so ill just make a whole new file. I might fix this later
Variable3=Variable2.read()
box = tk.Entry(root)
box.insert('0', Variable3)
box.grid(row=2,column=1, padx=5, pady=5)
box.focus_set()
Variable2.close()

button3 = ttk.Button(root, text='Save',
 command=lambda: clide())
button3.grid(row=2,column=2, padx=5, pady=5)

if Is_Closed_True() == True:
	jimmy()
	root.destroy()

root.mainloop()
