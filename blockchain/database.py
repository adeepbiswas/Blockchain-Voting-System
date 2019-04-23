import sqlite3

def addRecord(a,b,cds,d,e):
    con = sqlite3.connect("pubicLedger.db")
    c = con.cursor()

    c.execute(''' CREATE TABLE IF NOT EXISTS blockchain
             (sender_addr varchar(100), reciever_addr varchar(100),PoliticianID varchar(100),signature varchar(100),time varchar(100))''')

    #c.execute("INSERT INTO blockchain VALUES (?,?)" % str(var1),str(var2))
    c.execute("INSERT INTO blockchain VALUES ('{0}','{1}','{2}','{3}','{4}')".format(a,b,cds,d,e))

    for row in c.execute('SELECT * FROM blockchain'):
        print(row)

    con.commit()
    con.close()


