import paho.mqtt.client as mqtt

pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print("broker connected")

'''def hello:
    a=input("enter")
    i=1
    while(i>1):
        print(a)'''


pub_client.publish('gpcet/ai-b13','namasthe')