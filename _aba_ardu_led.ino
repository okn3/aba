byte val=0;
int led = 13;
int led2 = 12;
int led3 = 11;

void setup() { 
        pinMode(led, OUTPUT); 
        Serial.begin(9600);
}

void loop() {
        if(Serial.available() > 0){ 

                val = Serial.read();
                Serial.print(val); //for debug

                if(val == 'a'){
                        digitalWrite(led, HIGH);
                        delay(1000);              
                }
                
                else if(val == 'b'){   
                        digitalWrite(led2, HIGH);
                        delay(1000);              
 
                }
                else if(val == 'c'){   
                        digitalWrite(led3, HIGH);
                        delay(1000);              
 
                }
                
                else if(val == '0'){   
                        digitalWrite(led,LOW);
                        digitalWrite(led2,LOW);
                        digitalWrite(led3,LOW);
                        delay(1000);
                }
        }
}
