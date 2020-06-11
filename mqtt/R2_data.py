import paho.mqtt.client as mqtt
import csv

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("cvtgate/e50e6540-49e3-40d6-9c37-3fcc63400042/#") # Topic 을 구독한다.
                     #cvtgate/4fcec532-bd9d-4aa2-84d9-a87d027be887/# 로 하면 기상대 데이터
                     #cvtgate/d43e200a-3070-4c2b-b434-62af73c87130/#
                     #R1에 달린 구동기는 34db8790-c0b2-419c-9670-89348f50ba18
                     #R2는 e50e6540-49e3-40d6-9c37-3fcc63400042
                     #R3는 5b07fdb2-ff3d-48cc-bead-d1754fdd2a9e
                        
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    a=str(msg.payload)    
    s='"type": 500'
    results=a.find(s)

    if results > 160:
        print(results)
        b=a.split(",")
        fan=b[5].split(':')[2]
        co2_injection=b[0].split(':')[3]
        time=b[8].split('"')[3]
   
        R2_data=[time,fan,co2_injection]
    
        print(R2_data)
        f = open('R2_data.csv','a', newline='')
        wr = csv.writer(f)
        wr.writerow(R2_data)
        print('R2 data save')
        f.close()
    else:
        print(results)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("kist.jinong.co.kr") 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
