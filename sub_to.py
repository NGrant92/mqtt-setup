import paho.mqtt.client as mqttClient
import getpass
import json
import time
import sys

def on_message(client, userdata, message):
    print("message recieved")
    message_txt = message.payload.decode("utf-8")
    print("REPLY:", message_txt)

def on_connect(client, userdata, flags, rc):

    if rc == 0:
        global Connected
        Connected = True
    else:
        print("Connection failed")

with open("credentials.json") as cred_data:
    data_cred = json.load(cred_data)
    broker_address = data_cred["broker_address"]

Connected = False
# broker_address = "localhost"
port = 1883
user = "user"
password = "user"
local_user = getpass.getuser()

client = mqttClient.Client("mac-client")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(user, password)
client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)

try:
    topic = "mac"
    client.subscribe(topic, 2)
    print("Subscribed to: " + topic)

    # loop to keep listening on topic channels
    try:
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Shutdown: KeyboardInterrupt")
        client.disconnect()

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
