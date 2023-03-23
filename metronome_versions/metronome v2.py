import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

root = tk.Tk()

root.attributes("-fullscreen", False)

canvas = tk.Canvas(root, width=1920, height=1080, bg="white", highlightthickness=0)
# This is from the spec of the computer

canvas.pack()

dot = canvas.create_oval(0, 0, 40, 40, outline='')

mixer.init()
mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")


#bpm_input = int(input("BPM: "))
bpm_input = 60

def blinking_dot(i=0):
    colors = ("white", "red")
    canvas.create_oval(550,350,650,450,fill=colors[i])
    mixer.music.play()
    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)

blinking_dot()
root.mainloop()







# ---------------- #
import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
