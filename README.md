# MQTT TESTER
A module comprised of MQTT broker and a python script which simulates the behavior of a Kaatru IOT device.

# Local Setup
1. Clone this repository by running the following command
    ```
    git clone https://github.com/Kaatru-Senai/mqtt-tester.git
    ```
2. Once you have the files in your local environment, run the following command to run the containers
    ```
    docker compose up
    ```
Once the containers are up, the `MQTT Broker` can be accessed at host `localhost` and port `1883` and the python script will keep publishing data to the `mqtt/test` topic.