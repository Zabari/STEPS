#!/usr/bin/python
# raspberry pi nrf24l01 hub
# more details at http://blog.riyas.org
# Credits to python port of nrf24l01, Joao Paulo Barrac & maniacbugs original c library

from nrf24 import NRF24
import time, requests, json
from time import gmtime, strftime


oldStates = []
newStates = []

for n in range(12):
    oldStates.append(False)
    newStates.append(False)

pipes = [[0xf0, 0xf0, 0xf0, 0xf0, 0xe1], [0xf0, 0xf0, 0xf0, 0xf0, 0xd2]]

radio = NRF24()
radio.begin(0, 0,22,18) #set gpio 22 as CE pin
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x4c)
radio.setDataRate(NRF24.BR_250KBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(1)
radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()
radio.stopListening()

radio.printDetails()
radio.startListening()

def getData(s):# format of s: {4:1, 5:0}  
    e1,e2,v1,v2 = int(s[1:s.find(':')]),int(s[s.find(' '):s.rfind(':')]),int(s[s.find(':')+1:s.find(',')]),int(s[s.rfind(':')+1:s.rfind('}')])
    oldStates[e1],oldStates[e2] = newStates[e1],newStates[e2]
    newStates[e1],newStates[e2] = bool(v1),bool(v2)

def sendData():
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

while True:
    pipe = [0]
    while not radio.available(pipe, True):
        time.sleep(1000/1000000.0)
    recv_buffer = []
    radio.read(recv_buffer)
    out = ''.join(chr(i) for i in recv_buffer)
    print out
    getData(out)
    sendData()
