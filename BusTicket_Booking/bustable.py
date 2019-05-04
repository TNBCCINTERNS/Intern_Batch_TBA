import sqlite3
def Create_Table():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
 
    conn.execute('''CREATE TABLE BUS_SERVICE
         (BUSID INT PRIMARY KEY     NOT NULL,
         BUSNAME           TEXT    NOT NULL,
         ORIGIN            INT     NOT NULL,
         DESTINATION        CHAR(50),
         JOURNYDATE              TEXT,
         PRICE         REAL);''')
    print("Table created successfully")

    conn.close()
Create_Table()    



##################################################################################
    
'''

Button(root, text='Add Bus',width=25,bg='brown',fg='white').place(x=50,y=350)
Button(root, text='Remove Bus',width=25,bg='brown',fg='white').place(x=250,y=350)
Button(root, text='Fetch Data',width=25,bg='brown',fg='white').place(x=50,y=400)
Button(root, text='Update Data',width=25,bg='brown',fg='white').place(x=250,y=400)
'''

root.mainloop()
def Insert_Table(x1,x2,x3,x4,x5,x6,x7):
    import sqlite3
    conn = sqlite3.connect('test.db') 
   # print("Opened database successfully")    
    conn.execute("INSERT INTO test.db(x1,x2,x3,x4,x5,x6,x7) VALUES(?,?,?,?,?,?,?)",(x1,x2,x3,x4,x5,x6,x7))
    conn.commit()
   # print("record inserted")
    conn.close()
    
 
'''
def Create_Table():
    import sqlite3
    conn = sqlite3.connect('test.db')
  #  print("Opened database successfully")

    conn.execute('''CREATE TABLE BUS_SERVICE
         (BUSID INT PRIMARY KEY     NOT NULL,
         BUSNAME           TEXT    NOT NULL,
         ORIGIN            INT     NOT NULL,
         DESTINATION        CHAR(50),
         JOURNYDATE              TEXT,
         PRICE         REAL
         JOURNYTIME              TEXT);''')
   # print("Table created successfully")
    conn.close()
 '''
   

    
    
