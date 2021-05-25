import yaml
from decoder import from_ser
from encoder import to_ser


class yaml_my():
    def __init__(self):
        pass

    def dump(self,obj,fp):
        new_obj = to_ser(obj)
        with open(fp,'w') as yaml_file:
            yaml.dump(new_obj,yaml_file, default_flow_style=False)

    def dumps(self, obj):
        try:
            return yaml.dump(to_ser(obj),indent=5)
        except Exception:
            return None

    def load(self,fp):
        with open(fp,'r') as yaml_file:
            return from_ser(yaml.safe_load(yaml_file))

    def loads(self,s):
        return (from_ser(yaml.safe_load(s)))