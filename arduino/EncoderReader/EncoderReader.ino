#include <RotaryEncoder.h>;
int val = 0;
RotaryEncoder encoder1(A0,A1,5,6,3000);
RotaryEncoder encoder2(A4,A5,5,6,3000);

unsigned long lastMove1 = 0;
unsigned long lastMove2 = 0;
boolean on1 = false;
boolean on2 = false;

void setup()
{  
  Serial.begin(57600);
  
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
  
  if ((millis() - lastMove1) > 5000 && on1){
      on1 = false;
      Serial.print("Encoder 1 went idle. Offline for");
      Serial.println(millis() - lastMove1);
     // Serial.println(lastMove1 - millis()); 
  }
  
  if ((millis() - lastMove2) > 5000 && on2){
      on2 = false;
      Serial.print("Encoder 2 went idle. Offline for:");
      Serial.println(millis() - lastMove2);
     // Serial.println(lastMove1 - millis()); 
  }
  
  if (millis()%10000 == 0){
    // DATA TO SEND GO HERE
    // Escilator is 4 for up and 5 down for 5, send 
     Serial.println("Sending data...");
     String data = "{4: " + String(on1) + ", 5: " + String(on2) + "}" ;
     Serial.println(data);
     delayMicroseconds(50);

  }
  
  delayMicroseconds(50);
}

