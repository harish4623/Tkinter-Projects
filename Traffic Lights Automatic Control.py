from tkinter import *

# Create the main application window
play = Tk()
play.geometry("300x600")  # Set the window size
play.title("Traffic Lights-Automatic")  # Set the window title
play.configure(bg='lightblue')  # Set the background color

# Function to display the red light
def red():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='red')  # Red light ON
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Yellow light OFF
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Green light OFF

# Function to display the yellow light
def yellow():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Red light OFF
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='yellow')  # Yellow light ON
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Green light OFF

# Function to display the green light
def green():
    canvas1.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Red light OFF
    canvas2.create_oval(20, 20, 110, 110, outline='white', fill='white')  # Yellow light OFF
    canvas3.create_oval(20, 20, 110, 110, outline='white', fill='green')  # Green light ON

# Function to manage the light changes based on the counter
def intervals(c):
    if c > 15:  # If the counter is greater than 15, show the red light
        red()
    elif 10 < c <= 15:  # If the counter is between 10 and 15, show the yellow light
        yellow()
    elif 0 < c <= 10:  # If the counter is 10 or less, show the green light
        green()

    timerdata.config(text=c)  # Update the timer display with the current count
    if c > 0:
        # Schedule the next decrement of the counter after 1 second
        play.after(1000, counter, c - 1)
    else:
        # If the counter reaches 0, restart it from 25
        play.after(1000, counter, 25)

# Function to start the counter and control the traffic light sequence
def counter(data):
    intervals(data)

# Function triggered by the START button to initiate the traffic light sequence
def start():
    counter(25)  # Start the counter from 25

# START button to begin the traffic light sequence
Button(play, text='START', font=('calibri', 17), bg='gray', fg='white', width='10', height='1', command=start).place(x=90, y=500)

# Label to display the timer value
timerdata = Label(play, font=('calibri', 30, 'bold'), bg='black', fg='red')
timerdata.place(x=90, y=550)

# Manual control buttons for each light (for testing purposes)
Button(play, bg='red', width='8', height='2', command=red).place(x=20, y=60)  # Red light button
Button(play, bg='yellow', width='8', height='2', command=yellow).place(x=20, y=190)  # Yellow light button
Button(play, bg='green', width='8', height='2', command=green).place(x=20, y=320)  # Green light button

# Canvases representing each light in the traffic light
canvas1 = Canvas(play, width=130, height=130, bg='black')  # Canvas for the red light
canvas1.place(x=120, y=30)

canvas2 = Canvas(play, width=130, height=130, bg='black')  # Canvas for the yellow light
canvas2.place(x=120, y=160)

canvas3 = Canvas(play, width=130, height=130, bg='black')  # Canvas for the green light
canvas3.place(x=120, y=290)

# Start the main event loop to listen for events and update the GUI
play.mainloop()
