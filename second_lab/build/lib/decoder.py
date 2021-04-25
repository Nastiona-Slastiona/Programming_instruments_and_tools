import types
import builtins
from pickler import RedefinitionPickle


def from_ser( obj_dict):
    if not isinstance(obj_dict, dict): 
        return obj_dict
    elif obj_dict.get('type', None) in ('function', 'method'):
        try:
            data = RedefinitionPickle().loads(obj_dict.get('object in bytes', None))
            return get_function(data)
        except:
            return None
    else:
        try:
            return RedefinitionPickle().loads(obj_dict.get('object in bytes', None))
        except:
            class_name = obj_dict.get('name', 'SomeClass')
            class_attr = obj_dict.get('class_attr', {})
            for key, value in class_attr.items():
                class_attr[key] = from_ser(value)
            base_class = from_ser(obj_dict.get('base_class', ()))
            new_class = type(class_name, base_class, class_attr)
            if obj_dict.get('name', None):
                return new_class
            else:
                return new_class()    


def get_function( func_dict):
    for key, value in func_dict['FunctionType']['globals'].items():
            func_dict['FunctionType']['globals'][key] = from_ser(value)
    func_dict['FunctionType']['globals'].update({'__builtins__': builtins})
    func_code = types.CodeType(*func_dict['CodeType'].values())
    func_params = list(func_dict['FunctionType'].values())
    func = types.FunctionType(func_code, *func_params[:-2])
    func.__dict__.update(func_params[4]) 
    if func_params[5] is not None:
        func.__kwdefaults__ = func.__kwdefaults__
    return func
