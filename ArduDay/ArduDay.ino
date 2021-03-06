#include <Servo.h>
#include <Stepper.h>

Servo x, y;
Stepper myStepper(200, 8, 9,10, 11);


int timer = -1;

void setup() {
  pinMode(4, OUTPUT);
  digitalWrite(4, LOW);
  x.attach(2);
  Serial.begin(9600);

  
}

void loop() {
  if (Serial.available()){
    char i = Serial.read();
    if (i == 'l')
      x.write(x.read() + 1);
    if (i == 'r')
      x.write(x.read() - 1);

    if (i == 'u')
      myStepper.step(200);
    if (i == 'd')
      myStepper.step(-200);

    if (i == 'p'){
     timer = millis();
     digitalWrite(4, HIGH);
    }
  }
  if (millis() - timer >= 1000) {
    timer = -1;
    digitalWrite(4, LOW);
  }
}
