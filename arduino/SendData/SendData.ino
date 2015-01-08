//Libraries
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"
#include <RotaryEncoder.h>;


//for debugging if everything blows up
int serial_putc( char c, FILE * ) 
{
  Serial.write(c);
  return c;
} 

void printf_begin(void)
{
  fdevopen( &serial_putc, 0 );
}

//nRF24 set the pin 9 to CE and 10 to CSN/SS
//I'll put this all in the documentation... later
// Cables are:
//     SS       -> 10
//     MOSI     -> 11
//     MISO     -> 12
//     SCK      -> 13


//DECLARATIONS
int val = 0;
RotaryEncoder encoder1(A0,A1,5,6,3000);
RotaryEncoder encoder2(A4,A5,5,6,3000);

boolean esc1on = false;
unsigned long lastReport1 = 0;

boolean esc2on = false;
unsigned long lastReport2 = 0;


RF24 radio(9,10);

//we only need a write pipe, but I made two anyway
const uint64_t pipes[2] = { 
  0xF0F0F0F0E1LL,0xF0F0F0F0D2LL };

// here we can send up to 30 chars
char SendPayload[31] = "blah";

void setup(void) {
  Serial.begin(57600); //Debug 
  printf_begin();
  //nRF24 configurations
  radio.begin();
  radio.setChannel(0x4c);
  radio.setAutoAck(1);
  radio.setRetries(15,15);
  radio.setDataRate(RF24_250KBPS);
  radio.setPayloadSize(32);
  radio.openReadingPipe(1,pipes[0]);
  radio.openWritingPipe(pipes[1]);
  radio.startListening();
  radio.printDetails(); //for Debugging

  //Set pin 7 as a faux ground, b/c the other 2 are used.
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW);
}

void loop() {

  int enc1 = encoder1.readEncoder();
  int enc2 = encoder2.readEncoder();

  //check if encoder 1 is moving
  if(enc1 != 0) {
    Serial.println("in loop");
    esc1on = true;
    lastReport1 = millis();
    Serial.println("Encoder 1 Moved!");
  } 
  //check if encoder 2 is moving
  if(enc2 != 0) {
    esc2on = true;
    lastReport2 = millis();
    Serial.println("Encoder 2 Moved!");
  } 
  
  //check if no report in 5 seconds, if so, note it.
  if(lastReport1 - millis() > 5000){
    esc1on = false;
    Serial.println("Escalator 1 went offline.");
  }
  if(lastReport2 - millis() > 500000){
    esc2on = false;
    Serial.print("Escalator 2 went offline. (off for ");
    Serial.print(lastReport2);
    Serial.println("ms.");
  }
    
  delayMicroseconds(50);
  
  

  //Get status from sensor
  float status = getStatus();

  // Assign float to payload, here I'm sending it as string
  dtostrf(status,2,2,SendPayload);

  //add a tag
  strcat(SendPayload, " 3-5 Status");   // add a string

  //send out message
  radio.stopListening();
  bool ok = radio.write(&SendPayload,strlen(SendPayload));
  radio.startListening(); 
  Serial.println(SendPayload);  // for debugging

  // Send every 2 secs
  //delay(2000);  
}


// Getting status from escilator sensor
float getStatus(){
  //lol code will go here eventually
  return 1;

}



