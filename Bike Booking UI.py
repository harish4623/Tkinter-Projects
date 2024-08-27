import tkinter.messagebox
from tkinter import *
from tkinter import ttk

#GUI configuration
obj=Tk()
obj.title("Book your Dream Bike")
obj.geometry("1920x1080")
obj.configure(bg='aqua')

def values(selected):
    dropmenu2.set_menu(*options2.get(selected))

def book():
    tkinter.messagebox.showinfo('Booking Confirmation', 'Booking Successful! Thank You!')

Label(obj,text='Enter name : ',font=('calibri',17),bg='aqua').place(x=30,y=30)
Label(obj,text='Enter Address : ',font=('calibri',17),bg='aqua').place(x=30,y=80)
Label(obj,text='Enter Phone Number : ',font=('calibri',17),bg='aqua').place(x=30,y=130)
Label(obj,text='Enter E-Mail Address: ',font=('calibri',17),bg='aqua').place(x=30,y=180)

Label(obj,text='Select Brand : ',font=('calibri',17),bg='aqua').place(x=30,y=230)
options1=['Tvs','Yamaha','Hero','Honda','Royal Enfield','Jawa','Bajaj','Suzuki']
dropvar1=StringVar()
dropmenu1=ttk.OptionMenu(obj,dropvar1,'Select',*options1,command=values)
dropmenu1.place(x=250,y=235)

Label(obj,text='Select Model : ',font=('calibri',17),bg='aqua').place(x=30,y=280)
options2={
    'Tvs': ['Ronin 225','Apache RTR 200 4V','Apache RTR 160 4V','RR 310'],
    'Yamaha': ['R15','MT-15','FZ','RX 100'],
    'Hero': ['X Pulse','Xtreme 160 4V','Passion pro','Karizma'],
    'Honda': ['CB 650','Unicorn','Dio','Hornet'],
    'Royal Enfield': ['Classic 350','Thunder Bird 350','Hunter 350','Continental GT 650'],
    'Jawa': ['42 Bobber','42','Pereak','350'],
    'Bajaj': ['Pulsar 150','220F','Domianr 400','NS 200'],
    'Suzuki': ['Gixxer SF 250','Gixxer 150','V-Strom SX','Hayabusa ']
}
dropVar2=StringVar()
dropmenu2=ttk.OptionMenu(obj,dropVar2,'Select')
dropmenu2.place(x=250,y=285)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()

Entry(obj,textvariable=s1,font=('calibri',17)).place(x=250,y=30)
Entry(obj,textvariable=s2,font=('calibri',17)).place(x=250,y=80)
Entry(obj,textvariable=s3,font=('calibri',17)).place(x=250,y=130)
Entry(obj,textvariable=s4,font=('calibri',17)).place(x=250,y=180)

Button(obj,text='Book',font=('calibri',17),bg='white',fg='black',width='12',height='1',command=book).place(x=300,y=370)

obj.mainloop()

