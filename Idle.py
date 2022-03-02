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
    
def Idle():
	while True:
		Variable=open("Variable.txt", "r")
		a=Variable.read() #I dont know why I need to store "Variable.read()" in a seperate container but the if statement isnt able to read it if I dont.
		if a=='True':
			if checkIfProcessRunning('xmr-stak-rx'):
                            subprocess.run(['killall xmr-stak-rx'], shell=True) 
                            print("\n" + 'Made sure miner was dead. Ignore this message,\nits just a miner inconvenience (¬‿¬)' + "\n")
                            time.sleep(5)
                            print("\n" + 'Comeon, it was a good joke. So good infact,\nyou might need to read it again\nbecause of a bug that I dont feel like fixing.\nwhy are you launching the program via terminal anyway?' + "\n")
                            time.sleep(1)
			else :
				time.sleep(1)
		else:
                    Variable2=open("Variable2.txt","r")
                    Variable3=Variable2.read()
                    V=float(Variable3)
                    u=subprocess.check_output(['xprintidle'])
                    z=float(u) #if statements require float to work
                    if z >= V: 
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
s.start()


def warning():
	warn=tk.Tk()
	warn.geometry('300x25')
	warn.resizable(False,False)
	warn.title('WARNING')
	
	the_warning= tk.Label(warn, text='The input needs to be a number')
	the_warning.pack()

def jimmy():
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

	
	
root = tk.Tk()
root.geometry('425x75')
root.resizable(False, False)
root.title('Idle Miner')

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


root.mainloop()
