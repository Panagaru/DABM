int ledPin = 10;
char serialData;
const int sensorPin = A0;
float ilumination = 0.0;
int brightness;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorValue = analogRead(sensorPin); //lee el valor analogico del sensor
  ilumination = (5.0 * sensorValue) / 1024.0; //Convierte el valor leido
  Serial.println(ilumination); //imprime el valor de la temperatura puerto serial

  if (Serial.available()){
    brightness = Serial.read();
    analogWrite(ledPin,brightness);     
  }
  delay(50); //espera para leer de nuevo  
}
   
