from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("BUS RRSERVATION SYSTEM")

label_0 = Label(root, text="BUS SERVICE",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Enter your seat no:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select seat no') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=85,y=330)


entry_2 = Entry(root)
entry_2.place(x=240,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()

