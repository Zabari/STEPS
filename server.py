import sqlite3
L = ["up23", "down23","up24", "down24","up35", "down35","up46", "down46","up57", "down57","up68", "down68","up79", "down79"]
true=True
false=False
d={'data':[[6, false, 6421203495.845522],[6, true, 5421203495.845522],[13, true, 4421203495.845522],[12, false, 3421203495.845522],[10, false, 2421203495.845522],[3, true, 1421203495.845522],[8, true, 1421203492.84195],[5, false, 1421203498.848851],[0, true, 1421203500.851109],[2, true, 1421203489.83835], [9, true, 1421203489.838356],\
[4,true ,40432523.4324], [1, true, 1421203490.83955],[7, true, 1421203490.839556], [11, true, 1421203490.839558]]} #for testing
def updateDatabase(data):
    #uncomment below for debugging and comment line under it
    conn = sqlite3.connect('esc.db')
    #conn = sqlite3.connect('/var/www/FlaskApp/STEPS/esc.db')
    c=conn.cursor()
    try:
        c.execute('CREATE TABLE esc (name TEXT,time REAL, status BOOLEAN)')
    except:
        print
    for x in data["data"]:
        tup=(L[x[0]],x[2],x[1])
        #print tup
        c.execute('INSERT INTO esc VALUES (?,?,?)',tup)
        conn.commit()
    conn.close()

def fetchAll():
    d={}
    #uncomment below for debugging and comment line under it
    conn = sqlite3.connect('esc.db')
    #conn = sqlite3.connect('/var/www/FlaskApp/STEPS/esc.db')
    c=conn.cursor()
    for x in L:
        d[x]={}
        maxi=c.execute('SELECT max(time) FROM esc where name=?',(x,)).fetchall()[0][0]
        #print maxi
        d[x]['status']=(c.execute('SELECT status FROM esc WHERE name=? AND time=?',(x,maxi,)).fetchall()[-1][-1]==1)
        #d[x]['status']=(c.execute('SELECT * FROM esc WHERE name=? ORDER BY time',(x,)).fetchall()[-1][-1]==1)
        #print d[x]['status']
    conn.close()
    return d
def fetchTime(esci):
    ret=[]
    #uncomment below for debugging and comment line under it
    conn = sqlite3.connect('esc.db')
    #conn = sqlite3.connect('/var/www/FlaskApp/STEPS/esc.db')
    c=conn.cursor()
    ret=c.execute('SELECT time FROM esc WHERE name=? ORDER BY time',(L[esci],)).fetchall()
    for i in range(len(ret)):
        ret[i]=ret[i][0]
    conn.close()
    return ret
def fetchAllTime():
    ret=[]
    for i in range(len(L)):
        ret.append(fetchTime(i))
    return ret
def fetchStatus(esci):
    ret=[]
    #uncomment below for debugging and comment line under it
    conn = sqlite3.connect('esc.db')
    #conn = sqlite3.connect('/var/www/FlaskApp/STEPS/esc.db')
    c=conn.cursor()
    maxi=c.execute('SELECT max(time) FROM esc where name=?',(L[esci],)).fetchall()[0][0]
    ret=c.execute('SELECT status FROM esc WHERE name=? AND time=?',(L[esci],maxi,)).fetchall()[0][0]==1
    conn.close()
    return ret
def fetchStatusAll():
    ret=[]
    for i in range(len(L)):
        ret.append(fetchStatus(i))
    return ret
#updateDatabase(d) #for testing
#conn = sqlite3.connect('esc.db')
#c=conn.cursor()
#print c.execute('SELECT * FROM esc WHERE name=?',("up46",)).fetchall()
#conn.close()
#print fetchAll() #for testing
#print fetchAllTime()
#print fetchStatusAll()
