import paho.mqtt.client as mqttClient
import getpass
import json
import time
import sys

def on_message(client, userdata, message):
    message_txt = message.payload.decode("utf-8")
    print("REPLY: ", message_txt)

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

client = mqttClient.Client(local_user)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(user, password)
client.connect(broker_address, port=port)

client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)

try:
    message = sys.argv[1]
    topic = "mac"
    client.publish(topic, payload=message)
    print("\nMessage: " + message + "\nTopic: " + topic)
    client.disconnect()
    client.loop_stop()

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
