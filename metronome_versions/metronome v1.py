import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

root = tk.Tk()

canvas = tk.Canvas(root, width=1200, height=900, bg="white", highlightthickness=0)
canvas.pack()

dot = canvas.create_oval(0, 0, 40, 40, outline='')

mixer.init()
mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")


bpm_input = int(input("BPM: "))

def blinking_dot(i=0):
    colors = ("white", "red")
    canvas.create_oval(60,60,120,120,fill=colors[i])
    mixer.music.play()
    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)

blinking_dot()
root.mainloop()
