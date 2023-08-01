import json
import paho.mqtt.client as mqtt


class Streamer:
    """
    A data streamer which uses MQTT protocol to transfer data in realtime.
    """
    def __init__(self, host: str, port: int):
        """
        Initialises a streamer.
        :param host: hostname of the MQTT broker
        :param port: port of the MQTT broker
        """
        self.__host: str = host
        self.__port: str = port
        self.__client: mqtt.Client = mqtt.Client()
        self.__is_connected = False
        self.__debug = True

    def start(self):
        """
        Sets necessary callbacks and connects to the MQTT broker
        :return:
        """
        if not self.__is_connected:
            self.__client.on_connect = self.__handle_connect
            self.__client.on_disconnect = self.__handle_disconnect
            self.__client.connect(self.__host, self.__port, 60)
            self.__is_connected = True

    def push(self, topic: str, payload: dict):
        """
        Publishes the data to the specified topic.
        :param topic: Topic to which the data is published
        :param payload: Data which should be transmitted
        :return:
        """
        if not self.__is_connected:
            self.__print('ERROR: Failed to publish payload to topic [{topic}]'.format(topic=topic))
        else:
            self.__client.publish(topic, json.dumps(payload))
            self.__print('INFO: Published payload to topic [{topic}]'.format(topic=topic))

    def __handle_connect(self):
        """
        Called when connected to the MQTT Broker.
        :return:
        """
        self.__print('INFO: Connected to MQTT Broker')

    def __handle_disconnect(self):
        """
        Called when disconnected to the MQTT Broker.
        :return:
        """
        self.__is_connected = False
        self.__print('INFO: Disconnected from MQTT Broker')
        self.__print('INFO: Trying to reconnect...')
        self.start()

    def diable_print(self):
        """
        Disables logs from streamer.
        :return:
        """
        self.__debug = False

    def enable_print(self):
        """
        Enables logs from streamer.
        :return:
        """
        self.__debug = True

    def __print(self, *args, **kwargs):
        if self.__debug:
            print(*args, **kwargs)
