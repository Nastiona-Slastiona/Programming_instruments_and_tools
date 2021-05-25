import inspect
import io
import builtins
import base64
import types
import copyreg

from abc import ABC, abstractclassmethod
from pickle import Pickler, Unpickler


class RedefinitionPickler(Pickler):
    dispatch_table = copyreg.dispatch_table.copy()

    def __init__(self, obj):
        self.obj = obj
        self.f = io.BytesIO()
        super().__init__(file=self.f, protocol=None, fix_imports=True, buffer_callback=None)

    def dumps(self):
        super().dump(self.obj)
        res = self.f.getvalue()
        assert isinstance(res, (bytes, bytearray))
        return base64.b85encode(res).decode('ascii')


class RedefinitionUnpickler(Unpickler):
    def __init__(self, obj):
        self.obj = base64.b85decode(obj.encode('ascii'))
        self.f = io.BytesIO(self.obj)
        super().__init__(file=self.f, encoding="ASCII", fix_imports=True, errors="strict", buffers=None)

    def loads(self):
        if isinstance(self.obj, str):
            raise TypeError("Can't load pickle from unicode string")
        return super().load()


class RedefinitionPickle:
    @staticmethod
    def dumps(obj):
        try:
            return RedefinitionPickler(obj).dumps()
        except TypeError:
            None

    @staticmethod
    def loads(obj):
        try:
            return RedefinitionUnpickler(obj).loads()
        except TypeError:
            None