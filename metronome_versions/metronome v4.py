from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

root = tk.Tk()

root.attributes("-fullscreen", False)

window = tk.Canvas(root, width=1920, height=1080, bg="white", highlightthickness=0)
# This is from the spec of the computer

window.pack()

dot = window.create_oval(0, 0, 40, 40, outline='')

mixer.init()
mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")

###GETTING INPUT BPM FROM USER


v = StringVar() # Setting up input
bpm_input = None # Variable to hold the input later


L1 = Label(root, text="Input your BPM.")
L1.pack(side = LEFT)

E1 = Entry(window, textvariable = v, bd = 5)
E1.pack(side=RIGHT)

def userinput():
    global bpm_input
    a = E1.get()
    try:
        a = int(a)
        if not 40<=a<=300:
            print("problem 1")
            L1.config(text="Please input integer BPM in range 40 - 300.")
            
        else:
            L1.config(text="BPM accepted.")


    except:
        L1.config(text="Please input integer BPM in range 40 - 300.")

    # Update the variable
    inp = bpm_input

b = Button(window, text = 'Submit', command = userinput)
b.pack(side = BOTTOM)


###FLICKERING CIRCLE METRONOME
##
####bpm_input = int(input("BPM: "))
##bpm_input = 60
##
##def blinking_dot(i=0):
##    colors = ("white", "red")
##    window.create_oval(550,350,650,450,fill=colors[i])
##    mixer.music.play()
##    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)
##
##
##blinking_dot()

root.mainloop()


