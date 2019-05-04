from tkinter import*

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