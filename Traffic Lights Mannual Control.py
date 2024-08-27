from tkinter import *

# Create the main application window
play = Tk()
play.geometry("300x400")  # Set the window size
play.title("Traffic Lights-Manual")  # Set the window title
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

# Buttons to manually control the traffic lights
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
