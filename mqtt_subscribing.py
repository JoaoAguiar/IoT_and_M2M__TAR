import random

from paho.mqtt import client as mqtt_client
from sound import sound_temperature

# Set the parameters of MQTT Broker connection
broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}' # generate client ID with pub prefix randomly
username = 'emqx'
password = 'public'
topic1 = "python/led"
topic2 = "python/temp"

def connect_mqtt() -> mqtt_client:
    # This will be called after connecting the client
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.username_pw_set("emqx", "public")

    return client

def subscribe(client: mqtt_client):
    # This will be called after the client received messages from the MQTT Broker 
    # It will print out the name of subscribed topic and the received message
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        sound_temperature(msg.payload.decode(), msg.topic)

    # Client subscriptions
    client.subscribe(topic1)
    client.subscribe(topic2)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
