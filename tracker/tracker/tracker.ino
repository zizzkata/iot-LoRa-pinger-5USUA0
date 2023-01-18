#include <SPI.h>
#include <LoRa.h>

// Seeeduino XIAO
#define RX_PIN 7
#define TX_PIN 6
#define NSS_PIN 1
#define RST_PIN 0
#define DIO0_PIN 2

#define LORA_FREQ 433E6

#define BAUD_SERIAL 115200

#define BUTTON_PIN 3
#define SPEAKER_PIN 5

#define BUTTON_INTERVAL_MS 1000
#define LORA_INTERVAL_MS 500

static unsigned long timeWaitButton;
static unsigned long timeWaitLoRa;

static int address = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(SPEAKER_PIN, OUTPUT);

  Serial.begin(BAUD_SERIAL);

  LoRa.setPins(NSS_PIN, RST_PIN, DIO0_PIN);
  
  if (!LoRa.begin(LORA_FREQ)) {
    Serial.println("Starting LoRa failed!");
  }
}

void loraFunctionDecoder(String msg) {
  msg.trim();
  StringSplitter *strSplitter = new StringSplitter(msg, ';', 5);
  if (strSplitter->getItemCount() == 5) {
    Serial.println("Valid string LoRa");
    String code = strSplitter->getItemAtIndex(0);
    String source = strSplitter->getItemAtIndex(1);
    String dest = strSplitter->getItemAtIndex(2);
    String data = strSplitter->getItemAtIndex(3);
    String sign = strSplitter->getItemAtIndex(4);
    int codeInt = code.toInt();
    switch (codeInt) {
      case 5:
        sendLoRa(ping(source));
        break;
      case 10:
        sendLoRa();
        break;
      case 100:
        sendLoRa(setAddress(address));
        break;
      case 200:
        sendLoRa(sendLoRa(data));
        break;
      default:
        Serial.println("Code not recognized");
    }
  }
  delete strSplitter;
}

void handleLoRa() {
    String msg = "";
    // read packet
    while (LoRa.available()) {
      msg += (char)LoRa.read();
    }
    if (msg.length()) {
      loraFunctionDecoder(msg);
    }
}

void handleButton() {
  Serial.println("IAM PRESSED");
}

void loop() {
  // Check button
  if ((long)(millis() - timeWaitButton) > 0 && digitalRead(BUTTON_PIN) > 0) {
    handleButton();
    timeWaitButton += BUTTON_INTERVAL_MS;
  }

  // Check for LoRa msgs
  if ((long)(millis() - timeWaitLoRa) > 0 && (int packetSize = LoRa.parsePacket()) > 0) {
    handleLoRa();
    timeWaitLoRa += LORA_INTERVAL_MS;
  }
}
