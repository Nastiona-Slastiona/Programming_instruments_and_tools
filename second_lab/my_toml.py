import toml
from decoder import from_ser
from encoder import to_ser

class toml_my():
    def __init__(self):
        pass

    def dump(self,obj,fp):
        new_obj = to_ser(obj)
        with open(fp,'w') as toml_file:
            toml.dump(new_obj,toml_file)

    def dumps(self, obj):
        try:
            return toml.dumps(to_ser(obj))
        except Exception:
            return None

    def load(self,fp):
        with open(fp,'r') as toml_file:
            return from_ser(toml.load(toml_file))

    def loads(self,s):
        return (from_ser(toml.loads(s)))