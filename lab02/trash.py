from fabric_cls import SerializerFactory

Fabric = SerializerFactory()
ser = Fabric.create_serializer('json')
x = ser.load("file.json")
print(x)