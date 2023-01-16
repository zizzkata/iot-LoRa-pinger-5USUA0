#include <SoftwareSerial.h>
#include <StringSplitter.h>

#define RX_PIN 7
#define TX_PIN 6

#define BAUD_HUB 9600
#define BAUD_SERIAL 115200

#define SERIAL_HUB_INTERVAL_MS 2000
#define LORA_INTERVAL_MS 1000

static unsigned long timeWaitSerialHub;
static unsigned long timeWaitLoRa;

static int address = 0; // unset
static boolean registrationReceived = false;
static String registrationData = "";
static boolean stopCallReceived = false;
static String stopCallSignature = "";

SoftwareSerial serialHub(RX_PIN, TX_PIN);
// Receiving from hub                                          
// codes: 5  -> checkStatus         |         |         |
//        10 -> getAddress          |         |         |               
//        11 -> setAddress          | address |
//        ...
//        101 -> broadcastAddress   | address | No Data
//        ...
//        111 -> acceptRegister     | address | Pub Key | Sign?
//        112 -> declineRegister    | address | No Data
//        ...
//        120 -> deregisterTracker  | address | No Data | Sign
//        ...
//        200 -> pingTracker        | address | No Data | 
//        ...
//        210 -> callTracker        | address | ms      | Sign
//        211 -> stopTracker        | address |         | Sign
//        ...
//        310 -> getVoltage         | address | No Data | Sign

// Sending to hub ?
// codes: 5  -> checkStatus         | option  |
//        10 -> getAddress          | address | OK                 
//        11 -> setAddress          | address | OK
//        ...
//        101 -> broadcastAddress   | empty   | OK
//        ...
//        110 -> registerRequest    | empty   | Pub Key | Sign?
//        111 -> acceptRegister     | address | OK      | Sign?
//        112 -> declineRegister    | address | OK      
//        ...
//        120 -> deregisterTracker  | address | OK      | Sign
//        ...
//        200 -> pingTracker        | address | OK      | Sign
//        ...
//        210 -> callTracker        | address | OK      | Sign
//        211 -> stopTracker        | address | OK      | Sign
//        212 -> stopFromTracker    | address | OK      | Sign
//        ...
//        310 -> getVoltage         | address | Voltage | Sign

//        

void sendSerialHub(String msg) {
    serialHub.write((msg + '\n').c_str());
}

void serialHubFunctionDecoder(String msg) {
    msg.trim();
    StringSplitter *strSplitter = new StringSplitter(msg, ';', 4);
    if (strSplitter->getItemCount() == 4) {
        Serial.println("Valid string");
        String code = strSplitter->getItemAtIndex(0);
        String address = strSplitter->getItemAtIndex(1);
        String data = strSplitter->getItemAtIndex(2);
        String signature = strSplitter->getItemAtIndex(3);
        int codeInt = code.toInt();
        switch (codeInt) {
            case 5:
                sendSerialHub(getStatusCode());
                break;
            case 10:
                sendSerialHub(getAddress());
                break;
            case 11:
                sendSerialHub(setAddress(address));
                break;
            case 20:
                // Do smt
                break;
            default:
                Serial.println("Code not recognized");
        }
    }
    delete strSplitter;
    test(msg);
}

String getAddress() {
    return "10;" + String(address) + ";OK;";
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

String getStatusCode() {
    if (stopCallReceived) {
        return "5;1;;";
    } else if (registrationReceived) {
        return "5;2;;";
    }
    return "5;0;;";
}

void test(String msg) {
    //Serial.println(msg.length());
    for (int i=0 ;i < msg.length(); i++) {
      Serial.print("'");
      char c = msg.charAt(i);
      if (c == '\n') {
        Serial.print('\\n');
      } else if(c == '\r') {
        Serial.print('\\r');
      } else {
        Serial.print(c);
      }
      Serial.print("' ");
    }
    Serial.println("END");
}

void setup() {
    // Set up serial
    pinMode(RX_PIN, INPUT);
    pinMode(TX_PIN, OUTPUT);

    serialHub.begin(BAUD_HUB);

    // Set up timers
    timeWaitSerialHub = millis() + SERIAL_HUB_INTERVAL_MS;
    timeWaitLoRa = millis() + LORA_INTERVAL_MS;

    // Set up debugging
    Serial.begin(BAUD_SERIAL);
}

void loop() {
    // Check for msges from the hub
    if ((long)(millis() - timeWaitSerialHub) > 0 && serialHub.available() > 0) {
        serialHubFunctionDecoder(serialHub.readString());
        timeWaitSerialHub += SERIAL_HUB_INTERVAL_MS;
    }

    // Check for LoRa msgs
    if ((long)(millis() - timeWaitLoRa) > 0) {
        // Do smt
        timeWaitLoRa += LORA_INTERVAL_MS;
    }
}