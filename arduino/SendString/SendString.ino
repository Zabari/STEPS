//////Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <RF24_config.h>
#include <RotaryEncoder.h>;


//////Declarations
/// Globals
int serial_putc( char c, FILE * ) 
{
  Serial.write(c);
  return c;
} 
void printf_begin(void)
{
  fdevopen( &serial_putc, 0 );
}

char SendPayload[30] = "init";

int val = 0;
unsigned long lastMove1 = 0;
unsigned long lastMove2 = 0;
boolean on1 = false;
boolean on2 = false;

/// Radios
RF24 radio(9,10);
//we only need a write pipe, but I made two anyway
const uint64_t pipe[2] = { 
  0xF0F0F0F0E1LL,0xF0F0F0F0D2LL };

/// Rotary Encoders
RotaryEncoder encoder1(A0,A1,5,6,3000);
RotaryEncoder encoder2(A4,A5,5,6,3000);


///////////////////////////////////////////////////


void setup(void){
  Serial.begin(57600);
  printf_begin();
  //RF24 Config
  radio.begin();
  radio.setChannel(0x4c);
  radio.setAutoAck(1);
  radio.setRetries(15,15);
  radio.setDataRate(RF24_250KBPS);
  radio.setPayloadSize(32);
  radio.openReadingPipe(1,pipe[0]);
  radio.openWritingPipe(pipe[1]);
  radio.startListening();
  radio.printDetails(); //for Debugging

  //Set pin 7 as a faux ground, b/c the other 2 are used.
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW);
}


void loop()
{
  //Serial.print("Current Millis: ");
  //Serial.println(millis());
  int enc1 = encoder1.readEncoder();
  int enc2 = encoder2.readEncoder();

  int changevalue = 1;
  if(enc1) {
    lastMove1 = millis();
    on1 = true;    
    Serial.println("Encoder 1 Moved!");
  } 

  if(enc2) {
    lastMove2 = millis();
    on2 = true;
    Serial.println("Encoder 2 Moved!");
  } 

  if ((millis() - lastMove1) > 10000 && on1){
    on1 = false;
    Serial.print("Encoder 1 went idle. Offline for");
    Serial.println(millis() - lastMove1);
    // Serial.println(lastMove1 - millis()); 
  }

  if ((millis() - lastMove2) > 10000 && on2){
    on2 = false;
    Serial.print("Encoder 2 went idle. Offline for:");
    Serial.println(millis() - lastMove2);
    // Serial.println(lastMove1 - millis()); 
  }

  if (millis()%10000 == 0){
    // Escilator is 4 for up and 5 down for 5, send 
    Serial.println("Sending data...");
    String data = "{4:" + String(on1) + ", 5:" + String(on2) + "}";
    data.toCharArray(SendPayload, data.length()+1);

   // Serial.print("SendPayload[1] = ");
  //  Serial.println(SendPayload[1]);
    sendMsg(data);
    delayMicroseconds(50);

  }

  delayMicroseconds(50);
}


void sendMsg(String data){
   //Get payload from sensor

  //toAscii();

  //send out message
  radio.stopListening();
  bool ok = radio.write(&SendPayload,strlen(SendPayload));
  radio.startListening(); 

  // Send every 2 secs

  Serial.println("Sent String Successfully. Contents: " + data);
}


