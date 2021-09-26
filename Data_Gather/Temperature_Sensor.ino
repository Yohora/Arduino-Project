

const int sensorPin = A0;
const float baselineTemp = 25.0;


void setup(){

    Serial.begin(9600);
}

void loop(){

    int sensorVal = analogRead(sensorPin);
    float voltage = (sensorVal/1024.0)* 5.0;
    float temperature = (voltage - 0.5) * 100;
    Serial.println(temperature);

    delay(2000);

}








