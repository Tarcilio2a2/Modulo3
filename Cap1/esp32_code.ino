#define P_SENSOR_PIN 34   // Botão de nutrientes P
#define K_SENSOR_PIN 35   // Botão de nutrientes K
#define LDR_SENSOR_PIN 36 // Sensor LDR para pH
#define DHT_PIN 4         // Sensor DHT22 para umidade
#define RELAY_PIN 27      // Relé para acionar a irrigação

#include <DHT.h>
DHT dht(DHT_PIN, DHT22);

bool pSensorState = false;  // Estado do botão P
bool kSensorState = false;  // Estado do botão K
float pHValue = 7.0;        // Valor do pH baseado no LDR
float humidity = 0.0;       // Umidade do solo
int temperature = 0;        // Temperatura

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(P_SENSOR_PIN, INPUT);
  pinMode(K_SENSOR_PIN, INPUT);
  pinMode(LDR_SENSOR_PIN, INPUT);
  dht.begin();
}

void loop() {
  // Lê os sensores
  pSensorState = digitalRead(P_SENSOR_PIN); // Botão P
  kSensorState = digitalRead(K_SENSOR_PIN); // Botão K
  pHValue = analogRead(LDR_SENSOR_PIN) / 1024.0 * 14.0; // Lê o valor do LDR e converte para pH
  humidity = dht.readHumidity(); // Lê a umidade
  temperature = dht.readTemperature(); // Lê a temperatura
  
  // Lógica de decisão para irrigação
  if (humidity < 30 || pSensorState == LOW || kSensorState == LOW || pHValue < 5.5) {
    digitalWrite(RELAY_PIN, HIGH);  // Ativa a irrigação
  } else {
    digitalWrite(RELAY_PIN, LOW);   // Desativa a irrigação
  }

  // Envia os dados para o monitor serial (para posterior uso no Python)
  Serial.print("P: ");
  Serial.print(pSensorState);
  Serial.print(" | K: ");
  Serial.print(kSensorState);
  Serial.print(" | pH: ");
  Serial.print(pHValue);
  Serial.print(" | Humidity: ");
  Serial.print(humidity);
  Serial.println("%");

  delay(2000);  // Delay de 2 segundos antes de nova leitura
}
