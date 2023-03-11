#include <ArduinoJson.h>


void setup() {
// Open serial communications and wait for port to open:
Serial.begin(115200);
while (!Serial) {
; // wait for serial port to connect. Needed for native USB port only
}
}
void loop() { // run over and over
if (Serial.available()) {
  String jsonString;
jsonString = Serial.read();
StaticJsonDocument<200> doc;
  DeserializationError error = deserializeJson(doc, jsonString);

  if (error) {
    Serial.print("deserializeJson() failed: ");
    Serial.println(error.f_str());
    return;
  }
    const char* sensor = doc["sensor"];
  double value = doc["value"];

  Serial.print("Sensor: ");
  Serial.println(sensor);
  Serial.print("Value: ");
  Serial.println(value);


}
}
