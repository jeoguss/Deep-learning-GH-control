import paho.mqtt.client as mqtt
import csv

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("cvtgate/4fcec532-bd9d-4aa2-84d9-a87d027be887/#") # Topic 을 구독한다.
                     #cvtgate/4fcec532-bd9d-4aa2-84d9-a87d027be887/# 로 하면 기상대 데이터
                     #cvtgate/d43e200a-3070-4c2b-b434-62af73c87130/#
                     #R1에 달린 구동기는 34db8790-c0b2-419c-9670-89348f50ba18
                     #R2는 e50e6540-49e3-40d6-9c37-3fcc63400042
                     #R3는 5b07fdb2-ff3d-48cc-bead-d1754fdd2a9e
                     

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    a=str(msg.payload)
    s='"type": 100'
    results=a.find(s)
    print(results)
    
    if results > 200:  
        b=a.split(",")
    
        c=b[0].split('"')
        time=c[5]
    
        d=b[3].split('[')
        O_hum=d[1]
    
        e=b[6].split('[')
        O_tem=e[1]

        f=b[9].split('[')
        O_rad=f[1]

        g=b[12].split('[')
        wind_d=g[1]

        h=b[15].split('[')
        wind_v=h[1]

        i=b[18].split('[')
        rain=i[1]

        out_data=[time,O_hum,O_tem,O_rad,wind_d,wind_v,rain]
        print(out_data)
        f = open('write.csv','w', newline='')
        wr = csv.writer(f)
        wr.writerow(out_data)
        print('out data save')
        f.close()
    else:
        print(results)
        print('not saved')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
