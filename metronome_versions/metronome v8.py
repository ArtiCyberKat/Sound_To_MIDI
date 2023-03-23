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



import tkinter as tk
from pygame import mixer

root = tk.Tk()

root.attributes("-fullscreen", False)

window = tk.Canvas(root, width=500, height=500, bg="white")
# This is from the spec of the computer width=1920, height=1080

window.pack()



label1 = tk.Label(window, text="Recording voice")
label1.config(font=('helvetica', 14))
window.create_window(200, 25, window=label1)

label2 = tk.Label(window, text="Enter your BPM:")
label2.config(font=('helvetica', 10))
window.create_window(200, 100, window=label2)

entry1 = tk.Entry(root) 
window.create_window(200, 140, window=entry1)

label3 = tk.Label(root, text="BPM entered is an integer value between 40 and 300.")
label3.config(font=('helvetica', 8))
window.create_window(200, 100, window=label3)

label4 = tk.Label(root, text=":)")
label4.config(font=('helvetica', 8))
window.create_window(200, 210, window=label4)



dot = window.create_oval(0, 0, 40, 40, outline='')

mixer.init()
mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")

###BODY OF CODE

###GETS ALL WIDGETS
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    print(_list)

    return _list


bpm_input = None

def get_input_bpm():
    global bpm_input
    input_bpm = entry1.get()
    flag = False
    try:
        input_bpm = int(input_bpm)
        flag = True


    except:
        label4.config(text="Please input integer BPM in range 40 - 300.")


    # Update the variable
    if flag == True:
        if 40<=input_bpm<=300:
            label4.config(text="BPM accepted.")
            bpm_input = input_bpm
            button1.config(text="Continue", command=lambda: blinking_dot())



        else:
            label4.config(text="Please input integer BPM in range 40 - 300.")
    
button1 = tk.Button(text="Enter", command=get_input_bpm, bg="brown", fg="white", font=("helvetica", 9, "bold"))
window.create_window(200, 180, window=button1)




###FLICKERING CIRCLE METRONOME

def blinking_dot(i=0):
    widget_list = all_children(window)
    for item in widget_list:
        item.pack_forget()

    while True:
        colors = ("white", "red")
        window.create_oval(550,350,650,450,fill=colors[i])
        mixer.music.play()
        root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)

get_input_bpm()

root.mainloop()






