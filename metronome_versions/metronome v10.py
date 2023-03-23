##from tkinter import *
##import tkinter as tk
##import tkinter.ttk as ttk
##from pygame import mixer
##
#####SETTING UP WINDOW AND THINGS NEEDED FOR METRONOME
##root = tk.Tk()
##
##root.attributes("-fullscreen", False)
##
##window = tk.Canvas(root, width=1920, height=1080, bg="white")
### This is from the spec of the computer
##
##window.pack()
##
##dot = window.create_oval(0, 0, 40, 40, outline='')
##
##mixer.init()
##mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")
##
#####CLEARING window FUNCTION
##def clear_window():
##    for widget in window.winfo_children():
##        widget.destroy()
##
##
#####GETTING INPUT BPM FROM USER
##v = StringVar() # Setting up input
##bpm_input = None # Variable to hold the input later
##
##
##L1 = Label(root, text="Input your BPM.")
##L1.pack(side = LEFT)
##
##E1 = Entry(root, textvariable = v, bd = 5)
##E1.pack(side=RIGHT)
##
##def userinput():
##    global bpm_input
##    a = E1.get()
##    try:
##        a = int(a)
##        if not 40<=a<=300:
##            L1.config(text="Please input integer BPM in range 40 - 300.")
##            
##        else:
##            L1.config(text="BPM accepted.")
##            clear_window()
##            #blinking_dot()
##
##
##    except:
##        L1.config(text="Please input integer BPM in range 40 - 300.")
##
##    # Update the variable
##    inp = bpm_input
##
##b = Button(window, text = 'Submit', command = userinput)
##b.pack(side = BOTTOM)
##
##
##
##
#####FLICKERING CIRCLE METRONOME
##
##def blinking_dot(i=0):
##    print("hello")
##    colors = ("white", "red")
##    window.create_oval(550,350,650,450,fill=colors[i])
##    mixer.music.play()
##    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)
##
##
##
##
##root.mainloop()
##
##


### DOES NOT WORK



from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

root = tk.Tk()

root.geometry("1300x700")

##window = tk.Canvas(root, width=100, height=100, bg="white")
### This is from the spec of the computer width=1920, height=1080
##
##window.pack()

frame = Frame(root)
frame.pack()


label1 = tk.Label(frame, text="Recording voice", font=('helvetica', 14))
label1.pack(pady=10)

label2 = tk.Label(frame, text="Enter your BPM:", font=('helvetica', 10))
label2.pack(pady=10)

entry1 = tk.Entry(frame) 
entry1.pack(pady=10)

label3 = tk.Label(frame, text="BPM entered is an integer value between 40 and 300.", font=('helvetica', 8))
label3.pack(pady=10)

label4 = tk.Label(frame, text=":)", font=('helvetica', 8))
label4.pack(pady=10)



mixer.init()
mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")

###BODY OF CODE

###GETS ALL WIDGETS

bpm_input = None

def get_input_bpm():
    global bpm_input
    input_bpm = entry1.get()
    flag = False
    try:
        input_bpm = int(input_bpm)
        flag = True


    except:
        label4.config(text="You must input an INTEGER BPM in range 40 - 300.")


    # Update the variable
    if flag == True:
        if 40<=input_bpm<=300:
            label4.config(text="BPM accepted.")
            bpm_input = input_bpm
            button1.config(text="Continue", command=lambda: del_input_bpm())

        else:
            label4.config(text="You must input an integer BPM in RANGE of 40 - 300.")

    
button1 = tk.Button(frame, text="Enter", command=get_input_bpm, bg="brown", fg="white", font=("helvetica", 9, "bold"))
button1.pack(pady=10)

window = None

def del_input_bpm():
    global window
    frame.destroy()
    window = tk.Canvas(root, width=1300, height=700, bg="white")
    # These numbers are through trial and error to make sure area is as big as limits of screen.
    
    
    window.pack()
    blinking_dot()
    




###FLICKERING CIRCLE METRONOME

def blinking_dot(i=0):
    
    colors = ("white", "red")
    window.create_oval(600,300,700,400,fill=colors[i])
    # window.create_oval(x0,y0,x1,y1,fill=color)
    
    mixer.music.play()
    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)

get_input_bpm()

root.mainloop()
