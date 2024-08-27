import tkinter.messagebox
from tkinter import *

#GUI configuration
obj=Tk()
obj.title("Operations")
obj.geometry('1920x1080')
obj.configure(bg='lavender')

#Function Defenition
def add():
    a1=num1.get()
    a2=num2.get()
    result=a1+a2
    tkinter.messagebox.showinfo('Result','Addition Result : '+ str(result))

def sub():
    a1=num1.get()
    a2=num2.get()
    result=a1-a2
    tkinter.messagebox.showinfo('Result','Subtraction Result : '+str(result))

def multi():
    a1=num1.get()
    a2=num2.get()
    result=a1*a2
    tkinter.messagebox.showinfo('Result','Multiplication Result : '+str(result))

def divi():
    a1=num1.get()
    a2=num2.get()
    result=a1//a2
    tkinter.messagebox.showinfo('Result','Division Result : '+str(result))


#adding labels
Label(obj,text='Enter 1st number : ',font=('calibri',17),bg='lavender').place(x=30,y=30)
Label(obj,text='Enter 2nd number : ',font=('calibri',17),bg='lavender').place(x=30,y=80)

#declaring variable for textbox
num1=IntVar()
num2=IntVar()

#adding textboxes
Entry(obj,textvariable=num1,font=('calibri',17)).place(x=220,y=30)
Entry(obj,textvariable=num2,font=('calibri',17)).place(x=220,y=80)

#adding buttons
Button(obj,text='Addition',font=('calibri',17),bg='lavender',fg='black',width='12',height='1',command=add).place(x=220,y=170)
Button(obj,text='Subtraction',font=('calibri',17),bg='lavender',fg='black',width='12',height='1',command=sub).place(x=220,y=230)
Button(obj,text='Multiplication',font=('calibri',17),bg='lavender',fg='black',width='12',height='1',command=multi).place(x=220,y=290)
Button(obj,text='Division',font=('calibri',17),bg='lavender',fg='black',width='12',height='1',command=divi).place(x=220,y=350)

obj.mainloop()
