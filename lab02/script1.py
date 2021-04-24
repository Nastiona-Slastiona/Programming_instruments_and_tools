from fabric_cls import SerializerFactory
from classes import *


humanFam = family("Lora","Dan")

#s = human(42,'Lora',humanFam)

def hello():
    print("hello")

Fabric = SerializerFactory()
ser = Fabric.create_serializer("json")
ser1 = Fabric.create_serializer("yaml")
s = hello
ser.dump(s,"file.json")

x = ser.load("file.json")
print(x)
