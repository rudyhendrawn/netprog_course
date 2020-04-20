"""This script is an example of subscriber to CloudMQTT Broker"""

from urllib.parse import urlparse
import os
import paho.mqtt.client as mqtt

# Define event callbacks
def on_connect(mosq, obj, rc):
    print('Reconnect: {}'.format(str(rc)))

def on_message(mosq, obj, msg):
    # message = str(msg.payload)
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))

def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Mosquitto()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://m12.cloudmqtt.com:12075')
url = urlparse(url_str)

# After you successfully the publisher and subscribe code, 
# try to create your own MQTT broker by create an account at cloudmqtt.com

# Connect
mqttc.username_pw_set('dbkomngk', 'iWr3bpLbrojb')
mqttc.connect(url.hostname, url.port)

# Subscribe to a topic
mqttc.subscribe('python/', 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print('Reconnect: ' + str(rc))