##from tkinter import *
##import tkinter as tk
##import tkinter.ttk as ttk
##from pygame import mixer
##
##root = tk.Tk()
##
##root.attributes("-fullscreen", False)
##
##canvas = tk.Canvas(root, width=1920, height=1080, bg="white", highlightthickness=0)
### This is from the spec of the computer
##
##canvas.pack()
##
##dot = canvas.create_oval(0, 0, 40, 40, outline='')
##
##mixer.init()
##mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")
##
#####GETTING INPUT BPM FROM USER
##
##
##
##
### Function for getting Input
### from textbox and printing it 
### at label widget
##  
##def printInput():
##    inp = inputtxt.get(1.0, "end-1c")
##    print(inp)
##    return print
##  
### TextBox Creation
##inputtxt = tk.Text(canvas,
##                   height = 5,
##                   width = 20)
##  
##inputtxt.pack()
##  
### Button Creation
##printButton = tk.Button(canvas,
##                        text = "Print", 
##                        command = printInput)
##printButton.pack()
##  
### Label Creation
##lbl = tk.Label(canvas, text = "")
##lbl.pack()
##
##print(printInput())
####if not printInput().isnumeric():
####    lbl.config(text = "Please enter an integer between 40 and 300.")
##
##
##
##canvas.mainloop()
##
##
##
#####FLICKERING CIRCLE METRONOME
####
######bpm_input = int(input("BPM: "))
####bpm_input = 60
####
####def blinking_dot(i=0):
####    colors = ("white", "red")
####    canvas.create_oval(550,350,650,450,fill=colors[i])
####    mixer.music.play()
####    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)
####
####
####blinking_dot(i=0)
####
####root.mainloop()






from tkinter import *
master = Tk()
master.title('Title')

v = StringVar()

# Variable to hold the input
inp = None

L1 = Label(master, text = 'Name')
L1.pack(side = LEFT)

E1 = Entry(master, textvariable = v, bd = 5)
E1.pack(side = RIGHT)

def userinput():
    global inp
    a = E1.get()
    print (a)
    # Update the variable
    inp = a


b = Button(master, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


master.mainloop()
