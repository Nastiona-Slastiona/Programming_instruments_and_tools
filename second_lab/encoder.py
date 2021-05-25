import types
import inspect
import builtins
from decoder import from_ser
from pickler import RedefinitionPickle


def to_ser(obj):
    template = {
        'instanse': repr(obj),
        'name': _get_name(obj),
        'type': str(type(obj)).split('\'')[1],
        'base': _get_base(obj),
        'class_attr': _get_class_attr(obj),
        'func_param': _get_func_params(obj),
        'object in bytes': RedefinitionPickle().dumps(iffunc(obj))
    }
    return {key: value for key, value in template.items() if value}

def iffunc(obj):
    if isinstance(obj,(types.FunctionType, types.MethodType)):
        return function_to_obj(obj)
    else:
        return obj

def function_to_obj(obj):
    copy_code = _copy_code(obj)
    copy_func = _copy_func(obj)
    fglobals = {key: to_ser(value) for key, value 
        in copy_func['globals'].items() if key in copy_code['names']}
    copy_func.update({'globals': fglobals})
    func_dict = {'CodeType': copy_code, 'FunctionType': copy_func} 
    return func_dict

def _copy_code(obj):
        keys = [
            "argcount", "posonlyargcount", "kwonlyargcount", 
            "nlocals", "stacksize", "flags", "code", "consts",
            "names", "varnames", "filename", "name", "firstlineno",
            "lnotab", "freevars", "cellvars"
        ]
        values = [getattr(obj.__code__, "co_" + key) for key in keys]
        return dict(zip(keys, values))

def _copy_func(obj):
    keys = [
        "globals", "name", "defaults", 
        "closure", "dict", "kwdefaults"
    ]
    values = [getattr(obj, f'__{key}__') for key in keys]
    return dict(zip(keys, values))

def _get_base(obj):
    try:
        base = obj.__base__
        return to_ser(base) if base is not object else ()
    except:
        return None

def get_function(func_dict):
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

def _get_class_attr(obj):
    base_types = (int, float, bool, str, list, tuple, dict, set)
    if isinstance(obj, (*base_types, types.FunctionType, types.MethodType)):
        return None
    try: 
        all_attr = {**{key: value for key, value in inspect.getmembers(obj, 
                    predicate=inspect.isfunction)}, 
                    **{key: value for key, value in inspect.getmembers(obj) 
                    if not (key.startswith('__') and key.endswith('__'))}}
        for key, value in all_attr.items():
            if not isinstance(value, base_types):
                all_attr[key] = to_ser(value)
        return all_attr
    except AttributeError:
        return None

def _get_name(obj):
    try:
        return obj.__name__
    except:
        return None

def _get_func_params(obj):
    try:
        full_args = inspect.getfullargspec(obj)
        args_spec = (full_args.args, full_args.varargs, full_args.varkw, 
                    full_args.defaults, full_args.kwonlyargs, 
                    full_args.kwonlydefaults, full_args.annotations)
        return dict(zip(full_args._fields, args_spec))
    except:
        return None
