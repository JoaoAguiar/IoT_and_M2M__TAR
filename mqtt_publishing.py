import random
import time

from paho.mqtt import client as mqtt_client
from gpio import led
from temp import temperature

# Set the parameters of MQTT Broker connection
broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}' # generate client ID with pub prefix randomly
username = 'emqx'
password = 'public'
topic1 = "python/led"
topic2 = "python/temp"

def value(led_aux, temp_aux):
    led_status = led(led_aux, temp_aux)
    print("...", led_status)

    return led_status 

def get_temp():
    return temperature()

def connect_mqtt():
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

    return client

def publish(client):
    # Starting with the LEDS OFF
    led_aux = "LED OFF"

    # In this loop, and we will set the MQTT client publish function to send messages to the topics every second
    while True:
        led_aux = value(led_aux, get_temp())
        msg_1 = led_aux # msg_1 is going to have the led_status
        msg_2 = get_temp() # msg_2 is going to have the temperature
        
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
