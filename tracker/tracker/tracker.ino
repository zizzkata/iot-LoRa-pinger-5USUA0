#include <SPI.h>
#include <LoRa.h>
#include <StringSplitter.h>


// Seeeduino XIAO
#define RX_PIN 7
#define TX_PIN 6
#define NSS_PIN 1
#define RST_PIN 0
#define DIO0_PIN 2

#define LORA_FREQ 433E6

#define BAUD_SERIAL 115200

#define BUTTON_PIN 3
#define LED_PIN 4
#define SPEAKER_PIN 5

#define SPEAKER_HIGH 200 //based on what???
#define SPEAKER_LOW 0

#define BUTTON_INTERVAL_MS 1000
#define LORA_INTERVAL_MS 500

static int led_state = LOW;
static int button_state = LOW;

static unsigned long timeWaitButton;
static unsigned long timeWaitLoRa;

static int address = 2;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(SPEAKER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

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
      case 6:
        test();
        break;
      case 10:
        // sendLoRa();
        break;
      case 100:
        sendLoRa(setAddress(source));
        break;
      case 210:
        handleDeviceCall(dest, source);
        break;
      default:
        Serial.println("Code not recognized");
    }
  }
  delete strSplitter;
}

String ping(String source) {
    // if (source != "0") {
    return "6;" + String(address) + ";" + source + ";;";
    // }
    // return "500;;;;";
}

String handleDeviceCall(String dest, String source) {
  if (String(address) == dest) {
    alarmOn();
    sendLoRa("211;" + dest + ";" + source + ";OK;");
  }
}

String getAddress() {
  return "10;" + String(address) + ";OK;";
}
void test() {
  if (led_state) {
    analogWrite(SPEAKER_PIN,200);
  } else {
    analogWrite(SPEAKER_PIN, 200);
  }
  led_state = !led_state;
}

bool test_button() {
  
  if (analogRead(SPEAKER_PIN, SPEAKER_HIGH)){
    button_state = HIGH; 
  }
  if (digitalWrite(LED_PIN, HIGH)){
    button_state = HIGH;
  }
  if (button_state == HIGH){
    return HIGH; //button corresponds to led and speaker
  }

}

String setAddress(String recievedAddress) {
  int recievedAddressInt = recievedAddress.toInt();
  if (recievedAddressInt > -1) {
    address = recievedAddressInt;
    return "11;" + String(address) + ";OK;";
  } else {
    return "500;;ERROR;";
  }
}

String sendLoRa(String msg) {
  LoRa.beginPacket();
  LoRa.print(msg);
  LoRa.endPacket();
  return "20;;OK;";
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

// speaker actions
void turnSpeakerOn() {
  analogWrite(SPEAKER_PIN, SPEAKER_HIGH);
}

void turnSpeakerOff(){
  analogWrite(SPEAKER_PIN, SPEAKER_LOW);
}
// led actions
void turnLedOn() {
  digitalWrite(LED_PIN, HIGH);
}

void turnLedOff(){
  digitalWrite(LED_PIN, LOW);
}

void alarmOn() {
    bool pressed = test_button();
  if (pressed == LOW) { //no, not pressed
    turnSpeakerOn();
    turnLedOn();
  }
}

void alarmOff() {
    bool pressed = test_button();
    if (pressed == HIGH) { //yes, pressed
      turnLedOff();
      turnSpeakerOff;
    }
}

void handleButton() {
  Serial.println(analogRead(BUTTON_PIN));
}

void loop() {
  // Check button
  if ((long)(millis() - timeWaitButton) > 0 && digitalRead(BUTTON_PIN) > 0) {
    handleButton();
    timeWaitButton += BUTTON_INTERVAL_MS;
  }

  // Check for LoRa msgs
  if (((long)(millis() - timeWaitLoRa) > 0) && (LoRa.parsePacket() > 0)) {
    handleLoRa();
    timeWaitLoRa += LORA_INTERVAL_MS;
  }
}
