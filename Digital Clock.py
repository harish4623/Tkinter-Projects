from tkinter import *
import time

play=Tk()
play.geometry("420x200")
play.title("Digital Clock")
play.configure(bg="black")

def updatevalues():
    timerdata.config(text=time.strftime("%I:%M:%S"))
    timerdata.after(1000,updatevalues)

timerdata=Label(play,bg="black",fg='aqua',font=("arial",45,'bold'))
timerdata.pack()

Button(play,text="Show",width='8',height='2',bg="white",fg="black",relief="solid",command=updatevalues).pack()
play.mainloop()