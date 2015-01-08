import time, random, json, requests

oldStates = []
newStates = []
random.seed()

#can't work with actual raspi code, still using rng to simulate :(
def recieveData():
    for n in range(len(oldStates)):
        oldStates[n] = newStates[n]
    for n in range(len(newStates)):
        if random.random() > .9:
            newStates[n] = not newStates[n]

for n in range(12):
    oldStates.append(False)
    newStates.append(False)

while True:
    recieveData()
    dataOut = []
    for n in range(len(oldStates)):
        if oldStates[n] != newStates[n]:
            t = time.time()
            state = newStates[n]
            print "state %i changed to %d at time %d" % (n, state, t)
            dataOut.append([n,state,t])
    
    if dataOut:
    #if non-empty, send dataOut to server
        headers = {'content-type': 'application/json'}
        data = json.dumps({'data':dataOut})
        print data
        r = requests.post("http://0.0.0.0:8000/data", data=data, headers=headers)# replace with server address
    print oldStates
    print newStates
    print
    time.sleep(10)#only used to simulate arduinos sending data every 10 seconds
     
