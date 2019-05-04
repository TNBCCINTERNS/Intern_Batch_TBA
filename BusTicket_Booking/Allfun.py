
    
    from tkinter import*

    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    Image="file:///C:/Users/lenovo/Desktop/r.jpg"
    '''
    logo=PhotoImage(file="Image/tk.png")
    logo.pack()
    '''
    Button(root, text='RESERVATION',width=20,bg='brown',fg='white').place(x=100,y=380)
    Button(root, text='BUS MANAGEMENT',width=20,bg='brown',fg='white').place(x=250,y=380)
    root.mainloop()
    
    # ________________________________________________________________________________________________
    
  #  from tkinter import*
    
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    label=Label(root,text="From:",width=20,font=("bold",12))
    label.place(x=10,y=50)
    
    entry=Entry(root)
    entry.place(x=175,y=50)
    
    label_1=Label(root,text="Destination:",width=20,font=("bold",12))
    label_1.place(x=10,y=90)
    
    entry=Entry(root)
    entry.place(x=175,y=90)
    
    label_1=Label(root,text="Date:",width=20,font=("bold",12))
    label_1.place(x=10,y=130)
    
    entry=Entry(root)
    entry.place(x=175,y=130)
    
    
    Button(root, text='SEARCH',width=20,bg='red',fg='white').place(x=100,y=280)
    Button(root, text='BACK',width=20,bg='red',fg='white').place(x=250,y=280)
    root.mainloop()
    
    #________________________________________________________________________________________________________________
    
 #   from tkinter import *
    
    root = Tk()
    root.geometry('500x500')
    root.title("Registration Form")
    
    label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
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
    
    #_________________________________________________________________________    from tkinter import*
    
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    
    label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    
    label_1 = Label(root, text="Bus ID: ",width=20,font=("bold", 12))
    label_1.place(x=10,y=50)
    
    entry_1 = Entry(root)
    entry_1.place(x=175,y=50)
    
    label_2 = Label(root, text="Bus Name: ",width=20,font=("bold", 12))
    label_2.place(x=10,y=80)
    
    entry_2 = Entry(root)
    entry_2.place(x=175,y=80)
    
    label_3 = Label(root, text="From: ",width=20,font=("bold", 12))
    label_3.place(x=10,y=120)
    
    entry_3 = Entry(root)
    entry_3.place(x=175,y=120)
    
    
    label_4 = Label(root, text="Destination: ",width=20,font=("bold", 12))
    label_4.place(x=10,y=150)
    
    entry_4 = Entry(root)
    entry_4.place(x=175,y=150)
    
    
    label_5 = Label(root, text="Price: ",width=20,font=("bold", 12))
    label_5.place(x=10,y=180)
    
    entry_5 = Entry(root)
    entry_5.place(x=175,y=180)
    
    
    label_6 = Label(root, text="Date: ",width=20,font=("bold", 12))
    label_6.place(x=10,y=210)
    
    entry_7 = Entry(root)
    entry_7.place(x=175,y=210)
    
    
    label_8 = Label(root, text="Time: ",width=20,font=("bold", 12))
    label_8.place(x=10,y=240)
    
    entry_3 = Entry(root)
    entry_3.place(x=175,y=240)
    
    Button(root, text='Add Bus',width=25,bg='brown',fg='white').place(x=50,y=350)
    Button(root, text='Remove Bus',width=25,bg='brown',fg='white').place(x=250,y=350)
    Button(root, text='Fetch Data',width=25,bg='brown',fg='white').place(x=50,y=400)
    Button(root, text='Update Data',width=25,bg='brown',fg='white').place(x=250,y=400)
    
    root.mainloop()
    
    
    




                                
    