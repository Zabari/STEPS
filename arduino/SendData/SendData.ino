//LIBRARIES
#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

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
//I'll put this all in the documentation
// Cables are:
//     SS       -> 10
//     MOSI     -> 11
//     MISO     -> 12
//     SCK      -> 13

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
}

void loop() {

  //Get status from sensor
  float status = getStatus();

  // Assign float to payload, here I'm sending it as string
  dtostrf(status,2,2,SendPayload);

  //add a tag
  strcat(SendPayload, " 3-5 Status");   // add first string

  //send out message
  radio.stopListening();
  bool ok = radio.write(&SendPayload,strlen(SendPayload));
  radio.startListening(); 
  Serial.println(SendPayload);  // for debugging

  // Send every 2 secs
  delay(2000);  
}


// Getting status from escilator sensor
float getStatus(){
  //lol code will go here eventually
  return 1;

}

