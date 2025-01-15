const int boutonPin = 2;
const int ledRougePin = 9;
const int ledVertePin = 10;
const int loPlusPin = 5;
const int loMoinsPin = 6;
const int outputPin = A1;
const int dureeCapture = 10000;

bool captureEnCours = false;
unsigned long startTime;
unsigned long lastReadTime = 0;  
const int intervalleLecture = 20; 

void setup() {
  pinMode(boutonPin, INPUT_PULLUP);
  pinMode(ledRougePin, OUTPUT);
  pinMode(ledVertePin, OUTPUT);
  pinMode(loPlusPin, INPUT);
  pinMode(loMoinsPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(boutonPin) == LOW && !captureEnCours) {
    captureEnCours = true;
    startTime = millis();
    digitalWrite(ledVertePin, HIGH);
    digitalWrite(ledRougePin, LOW);
    Serial.println("Démarrage de la capture...");
  }

  if (captureEnCours) {
    if (millis() - lastReadTime >= intervalleLecture) {
      lastReadTime = millis();  // Mettre à jour le dernier temps de lecture

      if (digitalRead(loPlusPin) == HIGH || digitalRead(loMoinsPin) == HIGH) {
        Serial.println("Électrodes déconnectées !");
      } else {
        int valeurOutput = analogRead(outputPin);
        Serial.println(valeurOutput);
      }
    }

    if (millis() - startTime >= dureeCapture) {
      captureEnCours = false;
      digitalWrite(ledVertePin, LOW);
      digitalWrite(ledRougePin, HIGH);
      Serial.println("Capture terminée.");
    }
  }
}