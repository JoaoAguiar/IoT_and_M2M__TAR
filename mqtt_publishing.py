import random
import time

from paho.mqtt import client as mqtt_client
from gpio import led
from temp import temperature

broker = 'broker.emqx.io'
port = 1883

topic1 = "LED"
topic2 = "TEMPERATURE"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

def value(led_aux, temp_aux):
    led_status = led(led_aux, temp_aux)

    return led_status 

def get_temp():
    return temperature()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)

    return client

def publish(client):
    led_aux = "LED OFF"

    while True:
        led_aux = value(led_aux, get_temp())
        msg_1 = led_aux
        msg_2 = get_temp()
        
        result = client.publish(topic1, msg_1)
        status = result[0]

        if status == 0:
            print(f"Send `{msg_1}` to topic `{topic1}`")
        else:
            print(f"Failed to send message to topic {topic1}")
        
        result = client.publish(topic2, msg_2)
        status = result[0]

        if status == 0:
            print(f"Send `{msg_2}` to topic `{topic2}`")
        else:
            print(f"Failed to send message to topic {topic2}")
        
def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
