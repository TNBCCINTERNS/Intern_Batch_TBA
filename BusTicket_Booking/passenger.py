import sqlite3
def Create_Table():
    conn = sqlite3.connect('passenger.db') 
    print("Opened database successfully")
    conn.execute('''CREATE TABLE Passenger
         (
         FULL_NAME   CHAR(20)    NOT NULL, 
         AGE         INT         NOT NULL,
         SEAT_NO     INT       NOT NULL
         GENDER      CHAR(20)    NOT NULL,
         );''')
    print("Table created successfully")
    conn.close()
