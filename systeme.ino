#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5
#define RST_PIN 4

LiquidCrystal_I2C lcd(0x27, 20, 4);
MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // 1. Initialisation I2C et ecran LCD (SDA=21, SCL=22)
  Wire.begin(21, 22);
  lcd.init();
  lcd.backlight();
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("PORTAIL RICK & MORTY");
  lcd.setCursor(0, 1);
  lcd.print("Demarrage ESP32...");

  // 2. Initialisation SPI et RFID (SCK=18, MISO=19, MOSI=23, SS=5)
  SPI.begin(18, 19, 23, 5);
  rfid.PCD_Init();
  rfid.PCD_SetAntennaGain(rfid.RxGain_max);

  delay(1200);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("PORTAIL RICK & MORTY");
  lcd.setCursor(0, 1);
  lcd.print("DIMENSION : C-137");
  lcd.setCursor(0, 3);
  lcd.print("Scanner un badge...");

  Serial.println("Systeme pret. En attente de badge...");
}

void loop() {
  byte bufferATQA[2];
  byte bufferSize = sizeof(bufferATQA);

  MFRC522::StatusCode status = rfid.PICC_WakeupA(bufferATQA, &bufferSize);

  if (status == MFRC522::STATUS_OK) {
    if (rfid.PICC_ReadCardSerial()) {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("ACCES AUTORISE !");
      lcd.setCursor(0, 1);
      lcd.print("OUVERTURE PORTAIL...");
      
      lcd.setCursor(0, 2);
      lcd.print("UID:");
      for (byte i = 0; i < rfid.uid.size; i++) {
        lcd.print(" ");
        if (rfid.uid.uidByte[i] < 0x10) lcd.print("0");
        lcd.print(rfid.uid.uidByte[i], HEX);
      }

      Serial.print("Badge lu ! UID :");
      for (byte i = 0; i < rfid.uid.size; i++) {
        Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
        Serial.print(rfid.uid.uidByte[i], HEX);
      }
      Serial.println();

      rfid.PICC_HaltA();
      rfid.PCD_StopCrypto1();

      delay(3000);

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("PORTAIL RICK & MORTY");
      lcd.setCursor(0, 1);
      lcd.print("DIMENSION : C-137");
      lcd.setCursor(0, 3);
      lcd.print("Scanner un badge...");
    }
  }
  delay(100);
}