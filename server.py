import sqlite3
L = ["up23", "down23","up24", "down24","up35", "down35","up46", "down46","up57", "down57","up68", "down68","up79", "down79"]

def updateDatabase(data):
    conn = sqlite3.connect('esc.db')
    c=conn.cursor()
    try:
        c.execute('''CREATE TABLE esc (name TEXT,time REAL, status BOOLEAN)''')
    except:
        print
    for x in data["data"]:
        c.execute('INSERT INTO esc VALUES (?,?,?)',(L[x[0]],x[2],x[1]))
        conn.commit()
    conn.close()

def fetchAll():
    d={}
    for x in L:
        
        d[x]['status']=c.execute('SELECT * FROM esc WHERE name=? ORDER BY time',x).fetchall()[-1]['status']
