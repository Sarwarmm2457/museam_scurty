#include <SoftwareSerial.h>
#include <ArduinoJson.h>

SoftwareSerial espSerial(8, 9);
String str;
void setup(){
Serial.begin(115200);
espSerial.begin(115200);
delay(2000);
}
void loop()
{
StaticJsonDocument<200> doc;

  doc["sensor"] = "temperature";
  doc["value"] = 25.0;

  String jsonString;
  serializeJson(doc, jsonString);
espSerial.println(jsonString);
delay(1000);
}
