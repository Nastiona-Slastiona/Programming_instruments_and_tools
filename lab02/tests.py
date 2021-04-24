import unittest
from os import path, curdir
from my_json import json_my
from my_toml import toml_my
from my_yaml import yaml_my
from my_pickle import pickle_my
from classes import complex
from fabric_cls import SerializerFactory


def simple_f(a,b):
    return a+b

class SerializerTests(unittest.TestCase):
    def setUp(self):
        self.serializer = SerializerFactory()
        self.base_obj = {
            '1': 1,
            '2': 'string',
            '4':['abc', 213],
            '5':(34,'ref',[23,4],5)
            }
        self.function_obj = simple_f
        self.custom_complex_class = complex()

    def test_json(self):
        self.ser = self.serializer.create_serializer('json')

        self.ser.dump(self.base_obj,'TEST_JSON_base.json')
        check = self.ser.load('TEST_JSON_base.json')
        self.assertEqual(self.base_obj,check,"Eroror")

        self.ser.dump(self.function_obj,'TEST_JSON_function.json')
        check = self.ser.load('TEST_JSON_function.json')
        self.assertEqual(self.function_obj(5,6),check(5,6),"Eroror")

        self.ser.dump(self.custom_complex_class,'TEST_JSON_class.json')
        check = self.ser.load('TEST_JSON_class.json')
        self.assertEqual(self.custom_complex_class.method(5),check.method(5),"Eroror")

        check = self.ser.dumps(self.base_obj)
        self.assertEqual(self.ser.loads(check),self.base_obj)
        check = self.ser.dumps(self.function_obj)
        self.assertEqual(self.ser.loads(check)(5,6),self.function_obj(5,6))
        check = self.ser.dumps(self.custom_complex_class)
        self.assertEqual(self.ser.loads(check).method(5),self.custom_complex_class.method(5))

    def test_pickle(self):
        self.ser = self.serializer.create_serializer('pickle')

        self.ser.dump(self.base_obj,'TEST_PICKLE_base.json')
        check = self.ser.load('TEST_PICKLE_base.json')
        self.assertEqual(self.base_obj,check,"Eroror")

        self.ser.dump(self.function_obj,'TEST_PICKLE_function.json')
        check = self.ser.load('TEST_PICKLE_function.json')
        self.assertEqual(self.function_obj(5,6),check(5,6),"Eroror")

        self.ser.dump(self.custom_complex_class,'TEST_PICKLE_class.json')
        check = self.ser.load('TEST_PICKLE_class.json')
        self.assertEqual(self.custom_complex_class.method(5),check.method(5),"Eroror")

        check = self.ser.dumps(self.base_obj)
        self.assertEqual(self.ser.loads(check),self.base_obj)
        check = self.ser.dumps(self.function_obj)
        self.assertEqual(self.ser.loads(check)(5,6),self.function_obj(5,6))
        check = self.ser.dumps(self.custom_complex_class)
        self.assertEqual(self.ser.loads(check).method(5),self.custom_complex_class.method(5))

    def test_toml(self):
        self.ser = self.serializer.create_serializer('toml')

        self.ser.dump(self.base_obj,'TEST_TOML_base.json')
        check = self.ser.load('TEST_TOML_base.json')
        self.assertEqual(self.base_obj,check,"Eroror")

        self.ser.dump(self.function_obj,'TEST_TOML_function.json')
        check = self.ser.load('TEST_TOML_function.json')
        self.assertEqual(self.function_obj(5,6),check(5,6),"Eroror")

        self.ser.dump(self.custom_complex_class,'TEST_TOML_class.json')
        check = self.ser.load('TEST_TOML_class.json')
        self.assertEqual(self.custom_complex_class.method(5),check.method(5),"Eroror")

        check = self.ser.dumps(self.base_obj)
        self.assertEqual(self.ser.loads(check),self.base_obj)
        check = self.ser.dumps(self.function_obj)
        self.assertEqual(self.ser.loads(check)(5,6),self.function_obj(5,6))
        check = self.ser.dumps(self.custom_complex_class)
        self.assertEqual(self.ser.loads(check).method(5),self.custom_complex_class.method(5))

    def test_yaml(self):
        self.ser = self.serializer.create_serializer('yaml')

        self.ser.dump(self.base_obj,'TEST_YAML_base.json')
        check = self.ser.load('TEST_YAML_base.json')
        self.assertEqual(self.base_obj,check,"Eroror")

        self.ser.dump(self.function_obj,'TEST_YAML_function.json')
        check = self.ser.load('TEST_YAML_function.json')
        self.assertEqual(self.function_obj(5,6),check(5,6),"Eroror")

        self.ser.dump(self.custom_complex_class,'TEST_YAML_class.json')
        check = self.ser.load('TEST_YAML_class.json')
        self.assertEqual(self.custom_complex_class.method(5),check.method(5),"Eroror")

        check = self.ser.dumps(self.base_obj)
        self.assertEqual(self.ser.loads(check),self.base_obj)
        check = self.ser.dumps(self.function_obj)
        self.assertEqual(self.ser.loads(check)(5,6),self.function_obj(5,6))
        check = self.ser.dumps(self.custom_complex_class)
        self.assertEqual(self.ser.loads(check).method(5),self.custom_complex_class.method(5))

        
if __name__ == '__main__':
    unittest.main()