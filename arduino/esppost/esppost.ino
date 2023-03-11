#include <ArduinoJson.h>
#include <SoftwareSerial.h>

SoftwareSerial espSerial(2, 1); // RX, TX pins on NodeMCU
StaticJsonDocument<100> jsonBuffer;

void setup() {
  Serial.begin(115200);
  espSerial.begin(115200);
}

void loop() {
  while (espSerial.available()) {
    Serial.write(espSerial.read());
  }
}

void processData(char* data) {
  DeserializationError error = deserializeJson(jsonBuffer, data);
  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.c_str());
    return;
  }

  float h = jsonBuffer["humidity"];
  float t = jsonBuffer["temperature"];

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("% Temperature: "));
  Serial.print(t);
  Serial.println(F("C"));
}
