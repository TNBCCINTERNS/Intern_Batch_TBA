from tkinter import*
def bus():
   
  #  from tkinter import*
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    ''''
    Ima="file:///C:/Users/lenovo/Desktop/r.jpg"

    img=root.PhotoImage(image.open(path))
    panel=root.Label(root,image=img)
    panel.pack()
    '''
    Button(root, text='RESERVATION',width=20,bg='brown',fg='white',command=reservation).place(x=100,y=380)
    Button(root, text='BUS MANAGEMENT',width=20,bg='brown',fg='white',command=busmanagement).place(x=250,y=380)
    root.mainloop()
bus()    
    # ________________________________________________________________________________________________

def reservation():
 #   from tkinter import*
    def stop():
        root.destroy()
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    label=Label(root,text="From:",width=20,font=("bold",12))
    label.place(x=10,y=50)
    
    a=Entry(root)
    a.place(x=175,y=50)
    
    label_1=Label(root,text="Destination:",width=20,font=("bold",12))
    label_1.place(x=10,y=90)
    
    b=Entry(root)
    b.place(x=175,y=90)
    
    label_1=Label(root,text="Date:",width=20,font=("bold",12))
    label_1.place(x=10,y=130)
    
    c=Entry(root)
    c.place(x=175,y=130)
    
    Button(root, text='QUIT',width=20,bg='brown',fg='white',command=stop).place(x=10,y=440)
    
    
    
    Button(root, text='SEARCH',width=20,bg='red',fg='white',command=Display_Record).place(x=100,y=280)
    Button(root, text='BACK',width=20,bg='red',fg='white', command=bus).place(x=250,y=280)
    root.mainloop()
    
    #________________________________________________________________________________________________________________
 

def Display_Record(arg=None):
    def stop():
        root.destroy()
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    
    label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    
    r1= Label(root, text="BR123",width=20,font=("bold", 12))
    r1.place(x=175,y=50)
    r2= Label(root, text="DEV TRAVELERS",width=20,font=("bold", 12))
    r2.place(x=175,y=80)   
    r3=Label(root, text="PATNA",width=20,font=("bold", 12))
    r3.place(x=175,y=120)
    r4= Label(root, text="KOLKATA",width=20,font=("bold", 12))
    r4.place(x=175,y=150)
    r5= Label(root, text="500",width=20,font=("bold", 12))
    r5.place(x=175,y=180)
    r6= Label(root, text="12/02/2018",width=20,font=("bold", 12))
    r6.place(x=175,y=210)
    r7= Label(root, text="6:30",width=20,font=("bold", 12))
    r7.place(x=175,y=240)
    
    
    label_1= Label(root, text="Bus ID:=  BR-123 ",width=20,font=("bold", 12))
    label_1.place(x=10,y=50)
    
    label_2 = Label(root, text="Bus Name:=DEV TRAVELERS ",width=20,font=("bold", 12))
    label_2.place(x=10,y=80)
    
    label_3 = Label(root, text="From=PATNA",width=20,font=("bold", 12))
    label_3.place(x=10,y=120)
    
    label_4 = Label(root, text="Destination=KOLKATA ",width=20,font=("bold", 12))
    label_4.place(x=10,y=150)
    
    label_5 = Label(root, text="Price=500 ",width=20,font=("bold", 12))
    label_5.place(x=10,y=180)
    
    label_6 = Label(root, text="Date12/02/2018 ",width=20,font=("bold", 12))
    label_6.place(x=10,y=210)
    
    label_7 = Label(root, text="Time=9:30 ",width=20,font=("bold", 12))
    label_7.place(x=10,y=240)
    
    Button(root, text='booking',width=25,bg='brown',fg='white',command=passenger).place(x=50,y=300)
    
    Button(root, text='QUIT',width=20,bg='brown',fg='white',command=stop).place(x=10,y=440)
    
     

    
    R1=entry_a.get()
    r1.config(text=R1)
    
    
    R2=entry_b.get()
    r2.config(text=R2)
    
    
    R3=entry_c.get()
    r3.config(text=R3)
    
    
    
    R4=entry_d.get()
    r4.config(text=R4)
    
        
    
    R5=entry_e.get()
    r5.config(text=R5)
    
    
    
    R6=entry_f.get()
    r6.config(text=R6)
    
    
    
    R7=entry_g.get()
    r7.config(text=R7)
    
    root.mainloop()
    

    
def passenger():   
 #   from tkinter import *
    def stop():
        root.destroy()
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    
    label_0 = Label(root, text="BUS SERVICE",bg='red',fg="yellow",font="Helvetica 16 italic")
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
    
    
    entry_5 = Entry(root)
    entry_5.place(x=240,y=330)
    
    Button(root, text='FINISH',width=20,bg='brown',fg='white',command=Ticket_DEtails).place(x=180,y=380)
    Button(root, text='QUIT',width=20,bg='brown',fg='white',command=stop).place(x=10,y=440)
    
    root.mainloop()
    
    #___________________________________________________________________________________________


       
def Ticket_DEtails(arg=None):
    def stop():
        root.destroy()
    root = Tk()
    root.geometry('800x800')
    root.title("BUS RESERVATION SYSTEM")
    
    label=Label(root, text="your ticket details",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    
    label=Label(root, text="BUS details:-",bg='red',fg="green",font="Helvetica 12 italic")
    label.place(x=10,y=30)
    
    r1= Label(root, text="",width=20,font=("bold", 12))
    r1.place(x=175,y=50)
    r2= Label(root, text="",width=20,font=("bold", 12))
    r2.place(x=175,y=80)   
    r3=Label(root, text="",width=20,font=("bold", 12))
    r3.place(x=175,y=120)
    r4= Label(root, text="",width=20,font=("bold", 12))
    r4.place(x=175,y=150)
    r5= Label(root, text="",width=20,font=("bold", 12))
    r5.place(x=175,y=180)
    r6= Label(root, text="",width=20,font=("bold", 12))
    r6.place(x=175,y=210)
    r7= Label(root, text="",width=20,font=("bold", 12))
    r7.place(x=175,y=240)
    r8= Label(root, text="",width=20,font=("bold", 12))
    r8.place(x=175,y=270)
    r9= Label(root, text="",width=20,font=("bold", 12))
    r9.place(x=175,y=300)
    r10= Label(root, text="",width=20,font=("bold", 12))
    r10.place(x=175,y=370)
    
    
    label_1 = Label(root, text="Bus ID: ",width=20,font=("bold", 12))
    label_1.place(x=10,y=50)
    
    label_2 = Label(root, text="Bus Name: ",width=20,font=("bold", 12))
    label_2.place(x=10,y=80)
    
    label_3 = Label(root, text="From: ",width=20,font=("bold", 12))
    label_3.place(x=10,y=120)
    
    label_4 = Label(root, text="Destination: ",width=20,font=("bold", 12))
    label_4.place(x=10,y=150)
    
    label_5 = Label(root, text="Price: ",width=20,font=("bold", 12))
    label_5.place(x=10,y=180)
    
    label_6 = Label(root, text="Date: ",width=20,font=("bold", 12))
    label_6.place(x=10,y=210)
   
    label_7 = Label(root, text="Time: ",width=20,font=("bold", 12))
    label_7.place(x=10,y=240)
   
    label_8 = Label(root, text="PASSENGER DETAILS:- ",bg='red',fg="green",font="Helvetica 12 italic")
    label_8.place(x=10,y=270)
   
   #passenger details:-
   
    label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=10,y=300)
   
    label_2 = Label(root, text="Email",width=20,font=("bold", 10))
    label_2.place(x=10,y=330)
   
    label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=10,y=360)
   
    label_3 = Label(root, text="seat no:-",width=20,font=("bold", 10))
    label_3.place(x=10,y=390)
    
        
    Button(root, text='PRINT',width=20,bg='red',fg='white').place(x=10,y=410)
    Button(root, text='QUIT',width=20,bg='brown',fg='white',command=stop).place(x=10,y=440)
    
       
    R1=entry_a.get()
    r1.config(text=R1)
        
    
    R2=entry_b.get()
    r2.config(text=R2)
   
   
    R3=entry_c.get()
    r3.config(text=R3)
   
   
   
    R4=entry_d.get()
    r4.config(text=R4)
   
   
   
    R5=entry_e.get()
    r5.config(text=R5)
   
   
   
    R6=entry_f.get()
    r6.config(text=R6)
   
   
   
    R7=entry_g.get()
    r7.config(text=R7)
   
    R8=entry_1.get()
    r8.config(text=R8)
   
    R9=entry_2.get()
    r9.config(text=R9)
   
    R10=entry_3.get()
    r10.config(text=R10)
   
    R11=entry_4.get()
    r11.config(text=R11)
   
    root.mainloop()

        
    
    
    
def busmanagement():
   def stop():
        root.destroy()   
   root = Tk()
   root.geometry('500x500')
   root.title("BUS RESERVATION SYSTEM")
        #Create_Table()
   label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
   label.pack()
    
   label_1=Label(root, text="Bus ID: ",width=20,font=("bold", 12))
   label_1.place(x=10,y=50)
   
   entry_a=Entry(root)
   entry_a.place(x=175,y=50)
   
   label_2=Label(root, text="Bus Name: ",width=20,font=("bold", 12))
   label_2.place(x=10,y=80)
   
   entry_b=Entry(root)
   entry_b.place(x=175,y=80)
   
   label_3=Label(root, text="From: ",width=20,font=("bold", 12))
   label_3.place(x=10,y=120)
   
   entry_c=Entry(root)
   entry_c.place(x=175,y=120)
   
   
   label_4=Label(root, text="Destination: ",width=20,font=("bold", 12))
   label_4.place(x=10,y=150)
   
   entry_d=Entry(root)
   entry_d.place(x=175,y=150)
   
   
   label_5=Label(root, text="Price: ",width=20,font=("bold", 12))
   label_5.place(x=10,y=180)
   
   entry_e=Entry(root)
   entry_e.place(x=175,y=180)
        
        
   label_6=Label(root, text="Date: ",width=20,font=("bold", 12))
   label_6.place(x=10,y=210)

   entry_f=Entry(root)
   entry_f.place(x=175,y=210)
    
    
   label_7=Label(root, text="Time: ",width=20,font=("bold", 12))
   label_7.place(x=10,y=240)
    
   entry_g=Entry(root)
   entry_g.place(x=175,y=240)
        
   Button(root, text='Add Bus',width=25,bg='brown',fg='white').place(x=50,y=350)
     #Button(root, text='Remove Bus',width=25,bg='brown',fg='white',COMMAND=Delete_Table).place(x=250,y=350)
   Button(root, text='Fetch Data',width=25,bg='brown',fg='white',command=Display_Record).place(x=50,y=400)
        #Button(root, text='Update Data',width=25,bg='brown',fg='white',COMMAND=Update_Table).place(x=250,y=400)
   root.mainloop()



'''
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
    
    
    label_5 = Label(root, text="Date: ",width=20,font=("bold", 12))
    label_5.place(x=10,y=180)
    
    entry_5 = Entry(root)
    entry_5.place(x=175,y=180)
    
    
    label_6 = Label(root, text="Price: ",width=20,font=("bold", 12))
    label_6.place(x=10,y=210)
    
    entry_6 = Entry(root)
    entry_6.place(x=175,y=210)
    
    
    label_7 = Label(root, text="Time: ",width=20,font=("bold", 12))
    label_7.place(x=10,y=240)
    
    entry_7 = Entry(root)
    entry_7.place(x=175,y=240)
    
 #   Button(root, text='Add Bus',width=25,bg='brown',fg='white',COMMAND=Insert_Table(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),entry_6.get(),entry_7.get())).place(x=50,y=350)
    Button(root, text='Remove Bus',width=25,bg='brown',fg='white',COMMAND=Delete_Table).place(x=250,y=350)
    Button(root, text='Fetch Data',width=25,bg='brown',fg='white',COMMAND=Display_Table).place(x=50,y=400)
    Button(root, text='Update Data',width=25,bg='brown',fg='white',COMMAND=Update_Table).place(x=250,y=400)
    
    root.mainloop()
    '''
#################################################################################################    
'''
import sqlite3
def Create_Table():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
'''
#   conn.execute('''CREATE TABLE BUS_SERVICE(BUSID INT PRIMARY KEY     NOT NULL,BUSNAME           TEXT    NOT NULL, ORIGIN            INT     NOT NULL,DESTINATION        CHAR(50),    JOURNYDATE              TEXT, PRICE         REal, JOURNYTIME              TEXT);''') conn.close()
 
'''   
def Insert_Table(x1,x2,x3,x4,x5,x6,x7):
    conn = sqlite3.connect('bus.db') 
   # print("Opened database successfully")    
    conn.execute("INSERT INTO BUS_SERVICE(x1,x2,x3,x4,x5,x6,x7) VALUES(?,?,?,?,?,?,?)",(x1,x2,x3,x4,x5,x6,x7))
    conn.commit()
   # print("record inserted")
    conn.close()
    
    
def Display_Record():
    root = Tk()
    root.geometry('800x800')
    root.title("BUS RESERVATION SYSTEM")

    
    
    
    conn = sqlite3.connect('bus.db') 
  #  print("Opened database successfully")
    cur=conn.cursor()
    ###############new add  ##################################
    
'''
'''
showallrecords()
def showallrecords():
    data=read()
    for i,d in enumerate(data):
        Label(root,text=d[0]).grid(row=i+1,col=0)
        Label(root,text=d[1]).grid(row=i+1,col=1)
        Label(root,text=d[2]).grid(row=i+1,col=2)
        Label(root,text=d[3]).grid(row=i+1,col=3)
        Label(root,text=d[4]).grid(row=i+1,col=4)
        Label(root,text=d[5]).grid(row=i+1,col=5)
        Label(root,text=d[6]).grid(row=i+1,col=6)
        Label(root,text=d[7]).grid(row=i+1,col=7)
def read():
    cur.excute("SELECT * FROM BUS_SERVICE")
    return cur.fetchall()
#root.mainloop()


    
    
    
    ######new add end #################################
  #  conn.close()


def Update_table():
    conn = sqlite3.connect('bus.db') 
    print("Opened database successfully")    
    conn.execute("update BUS_SERVICE set ID= ?, where NAME=?")
    conn.commit()
    print("total row update= ",conn.total_changes)
    conn.close()


def Delete_table():
    conn = sqlite3.connect('bus.db') 
    print("Opened database successfully")    
    conn.execute("DELETE FROM BUS_SERVICE where NAME=?")
    conn.commit()
    print("total row deleted= ",conn.total_changes)
    conn.close()
  
    
def Search_table():
    conn = sqlite3.connect('bus.db') 
    print("Opened database successfully")    
    conn.execute("SELECT * FROM BUS_SERVICE where ORIGIN=? AND DESTINATION=?")
    conn.close()

'''