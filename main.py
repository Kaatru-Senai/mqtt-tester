import time

import paho.mqtt.client as mqtt
import json
import random
from time import sleep
from threading import Thread


# The callback for when the client receives a CONNACK response from the server.
def on_connect(_, __, ___, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)
    Thread(target=start_publishing).start()


# The callback for when a PUBLISH message is received from the server.
def on_message(_, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# A function to keep pusblishing data every 5 seconds.
def start_publishing():
    client.publish(topic, json.dumps(gen_data()))
    sleep(5)
    start_publishing()


# A function to generate data packet.
def gen_data():
    global pid_
    pid_ += 1
    print(pid_)
    return {
        "pID": pid_,
        "dID": "LM11",
        "rHeap": 117288,
        "lHeap": 106640,
        "dTS": int(time.time_ns() / 1e9),
        "dUT": 1282,
        "lat": 13.042021 + random.random() * (13.132310 - 13.042021),
        "nso": "N",
        "long": 80.182343 + random.random() * (80.304565 - 80.182343),
        "ewo": "E",
        "alt": 29.5,
        "sog": 0,
        "cog": 0,
        "hdop": 1.11,
        "vdop": 0,
        "pdop": 0,
        "age": 137,
        "ax": -564,
        "ay": 16444,
        "az": -708,
        "gx": -324,
        "gy": -14,
        "gz": -70,
        "accTemp": random.randint(0, 50),
        "dPM1": random.randint(0, 300),
        "dPM2": random.randint(0, 200),
        "dPM10": random.randint(0, 300),
        "temp": random.randint(0, 50),
        "rh": random.randint(0, 100)
    }


pid_ = 0
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
topic = 'mqtt/test'

client.connect("broker", 1883, 60)

client.loop_forever()
