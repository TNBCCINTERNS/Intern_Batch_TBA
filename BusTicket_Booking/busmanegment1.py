from tkinter import*
root = Tk()
root.geometry('1000x1000')
root.title("BUS RESERVATION SYSTEM")
#Create_Table()
label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
label.pack()
    
label_1=Label(root, text="Bus ID: ",width=20,font=("bold", 12))
label_1.place(x=10,y=50)
    
entry_1=Entry(root)
entry_1.place(x=175,y=50)
    
label_2=Label(root, text="Bus Name: ",width=20,font=("bold", 12))
label_2.place(x=10,y=80)
        
entry_2=Entry(root)
entry_2.place(x=175,y=80)
    
label_3=Label(root, text="From: ",width=20,font=("bold", 12))
label_3.place(x=10,y=120)
    
entry_3=Entry(root)
entry_3.place(x=175,y=120)
    
    
label_4=Label(root, text="Destination: ",width=20,font=("bold", 12))
label_4.place(x=10,y=150)
    
entry_4=Entry(root)
entry_4.place(x=175,y=150)
    
    
label_5=Label(root, text="Price: ",width=20,font=("bold", 12))
label_5.place(x=10,y=180)
    
entry_5=Entry(root)
entry_5.place(x=175,y=180)
    
    
label_6=Label(root, text="Date: ",width=20,font=("bold", 12))
label_6.place(x=10,y=210)
    
entry_6=Entry(root)
entry_6.place(x=175,y=210)
    
    
label_7=Label(root, text="Time: ",width=20,font=("bold", 12))
label_7.place(x=10,y=240)
    
entry_7=Entry(root)
entry_7.place(x=175,y=240)

Button(root, text='Add Bus',width=25,bg='brown',fg='white').place(x=50,y=350)
    #Button(root, text='Remove Bus',width=25,bg='brown',fg='white',COMMAND=Delete_Table).place(x=250,y=350)
#Button(root, text='Fetch Data',width=25,bg='brown',fg='white',command=Display_Record).place(x=50,y=400)
    #Button(root, text='Update Data',width=25,bg='brown',fg='white',COMMAND=Update_Table).place(x=250,y=400)
root.mainloop()
'''
r1= Label(root, text="",width=20,font=("bold", 12))
r1.place(x=175,y=50)
r2= Label(root, text="",width=20,font=("bold", 12))
r2.place(x=175,y=80)
r3= Label(root, text="",width=20,font=("bold", 12))
r3.place(x=175,y=120)
r4= Label(root, text="",width=20,font=("bold", 12))
r4.place(x=175,y=150)
r5= Label(root, text="",width=20,font=("bold", 12))
r5.place(x=175,y=180)
r6= Label(root, text="",width=20,font=("bold", 12))
r6.place(x=175,y=210)
r7= Label(root, text="",width=20,font=("bold", 12))
r7.place(x=175,y=240)
'''


  

def Display_Record(arg=None):
   
    root = Tk()
    root.geometry('500x500')
    root.title("BUS RESERVATION SYSTEM")
    
    label=Label(root, text="BUS SERVICES",bg='red',fg="yellow",font="Helvetica 16 italic")
    label.pack()
    
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

    label_11 = Label(root, text="Bus ID: ",width=20,font=("bold", 12))
    label_11.place(x=10,y=50)

    label_22 = Label(root, text="Bus Name: ",width=20,font=("bold", 12))
    label_22.place(x=10,y=80)

    label_33 = Label(root, text="From: ",width=20,font=("bold", 12))
    label_33.place(x=10,y=120)

    label_44 = Label(root, text="Destination: ",width=20,font=("bold", 12))
    label_44.place(x=10,y=150)

    label_55 = Label(root, text="Price: ",width=20,font=("bold", 12))
    label_55.place(x=10,y=180)

    label_66 = Label(root, text="Date: ",width=20,font=("bold", 12))
    label_66.place(x=10,y=210)

    label_77 = Label(root, text="Time: ",width=20,font=("bold", 12))
    label_77.place(x=10,y=240)

    R1=entry_1.get()
    r1.config(text=R1)
        
    r2= Label(root, text="",width=20,font=("bold", 12))
    r2.place(x=175,y=80)
    
    R2=entry_2.get()
    r2.config(text=R2)
    
    
    R3=entry_3.get()
    r3.config(text=R3)
    
    
    
    R4=entry_4.get()
    r4.config(text=R4)
    
    
    
    R5=entry_5.get()
    r5.config(text=R5)
    
    
    
    R6=entry_6.get()
    r6.config(text=R6)



    R7=entry_7.get()
    r7.config(text=R7)
    root.mainloop()
    






'''
from tkinter import * 
def raj():
    
    root = Tk()
    # Create the Entry widget
    myEntry = Entry(root, width=20)
    myEntry.pack()
    result = myEntry.get()
    # Create the Enter button
    enterEntry = Button(root, text= "Enter", command=returnEntry(result))
    enterEntry.pack(fill=X)

# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)




def returnEntry(result):
    resultLabel.config(text=result)
root.geometry("+750+400")
root.mainloop()
'''