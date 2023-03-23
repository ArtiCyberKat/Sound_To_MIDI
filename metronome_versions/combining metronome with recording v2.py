###IMPORTS FOR USUAL TKINTER + SOUND FOR METRONOME
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from pygame import mixer

###IMPORTS FOR RECORDING
from tkinter import messagebox
import sounddevice as sd
import queue
import soundfile as sf
import threading

## EXPLANATION OF WHERE OUTPUT IS PUT FOR TKINTER.
# Root is permanent. If this is destroyed, code will be terminated.
# Window is in the middle of the two. It is used as the canvas for shapes.
# Frames can be destroyed whenever and more widgets (buttons, entry inputs)
# can be added into the space and destroyed too, as long as it is in the frame.

# There are two ways to create things: .pack() and .grid_layout()
# I chose .pack() because I understood it far quicker than the grid
# and it seems easy to use.
# Packing or Grid Layout tells the widget that it actually is in the space.


root = tk.Tk()

root.geometry("1300x700")


# Creating the frame where everything will be.
frame = Frame(root)
frame.pack()

# These are all the widgets for the first page.
label1 = tk.Label(frame, text="Recording voice", font=('helvetica', 14))
label1.pack(pady=10)

label2 = tk.Label(frame, text="Enter your BPM:", font=('helvetica', 10))
label2.pack(pady=10)

entry1 = tk.Entry(frame)
entry1.focus_set()
entry1.pack(pady=10)

label3 = tk.Label(frame, text="BPM entered is an integer value between 40 and 300.", font=('helvetica', 8))
label3.pack(pady=10)

label4 = tk.Label(frame, text=":)", font=('helvetica', 8))
label4.pack(pady=10)


# This is kept in as a reminder that, although was a main part of the major draft of this programme, it eventually was not needed.
# mixer.init()
# mixer.music.load("C:\$$$AUDIO FILES\metronome_click_3.wav")


###MAIN BODY OF CODE

# Getting the BPM
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

    if flag == True:
        if 40<=input_bpm<=300:
            label4.config(text="BPM accepted.")
            bpm_input = input_bpm
            button1.config(text="Continue", command=lambda: del_frame())

        else:
            label4.config(text="You must input an integer BPM in RANGE of 40 - 300.")

    
button1 = tk.Button(frame, text="Enter", command=get_input_bpm, bg="brown", fg="white", font=("helvetica", 9, "bold"))
button1.pack(pady=10)



# Destroying previous frame to get rid of all old widgets
def del_frame():
    frame.destroy()
    button_to_start()


# Making new frame again to put in new button.
frame1 = None
button2 = None
def button_to_start():
    global frame1
    global button2
    frame1 = Frame(root)
    frame1.pack()
    button2 = tk.Button(frame1, text="START METRONOME AND RECORDING", command=lambda: create_window(), bg="brown", fg="white", font=("helvetica", 9, "bold"))
    button2.pack(pady=10)

# 
window = None
def create_window():
    global window
    window = tk.Canvas(root, width=1300, height=700, bg="white")
    # These numbers are through trial and error to make sure area is as big as limits of the screen without asking the code to go full screen.
    # I do not want the code to go full screen because it is then hard to exit the output Tkinter screen (without using the Alt+Tab method to switch
    # between tabs because the exit X disappears from the output window).
    window.pack()
    threading_rec(1)



###THIS IS THE BEGINNING OF THE RECORDING AUDIO SEQUENCE
    
q = queue.Queue()
# Create a queue to contain audio data. First bit of data in goes out first.
recording = False
file_exists = False

# Fit data into queue.
def callback(indata, frames, time, status):
    q.put(indata.copy())

# Functions to record and stop recording audio.
# The recording is done as a thread to prevent it being the main process.
def threading_rec(x):
    if x == 1:
        # If recording is selected, then the thread is activated
        t1=threading.Thread(target= record_audio)
        blinking_dot()
        t1.start()
    elif x == 2:
        # To stop, set the flag to false
        global recording
        recording = False
        messagebox.showinfo(message="Recording finished")
        stop_blinking_dot()

# This is to get the input stream into a file.
def record_audio():
    global recording
    recording = True
    global file_exists

    messagebox.showinfo(message="Recording Audio. Sing into the microphone.")

    with sf.SoundFile("C:\$$$AUDIO FILES\MY_OWN.wav", mode='w', samplerate=44100,
                      channels=2) as file:
        # Create an input stream to record audio without a preset time.
        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while recording == True:
                # Set variable to True to allow playing audio later
                file_exists = True
                # Writing into file
                file.write(q.get())  

###FLICKERING CIRCLE METRONOME

def blinking_dot(i=0):
    global button2
    button2.config(text="STOP RECORDING", command=lambda: threading_rec(2))
    colors = ("white", "red")
    window.create_oval(600,300,700,400,fill=colors[i])
    # window.create_oval(x0,y0,x1,y1,fill=color)
    
    # mixer.music.play()
    # I realised, after v1 where you could hear the metronome, that this was a bad idea
    # because you could still hear the metronome in the recording, which would affect the MIDI output when analysed.
    
    root.after(int((60/bpm_input)*1000), blinking_dot, 1-i)

    

##frame3 = None
def stop_blinking_dot():
    button2.destroy()
    window.destroy()
    root.destroy() # To delete later when everything else works
##    global fram3
##    frame3 = Frame(root)
##    frame3.pack()

get_input_bpm()

root.mainloop()
