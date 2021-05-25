from arguments import get_files
from fabric_cls import SerializerFactory


def working_with_code(files, obj):
    ser1 = SerializerFactory()
    ser1 = ser1.create_serializer(files.get(list(files)[0]))
    ser2 = SerializerFactory()
    ser2 = ser2.create_serializer(files.get("extension"))
    obj = ser1.load(list(files)[0])
    ser2.dump(
        ser2,list(files)[0].split('.')[0] + 
        '.' + files.get("extension")
        )   

def main():
    files = get_files()
    obj = ''

    if (files.get(list(files)[0]) == files.get("extension")):
        print("The extension of the file is already done")
    else:
        working_with_code(files, obj)

if __name__ == "__main__":
    main()