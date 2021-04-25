import json
from decoder import from_ser
from encoder import to_ser

class json_my:

    def __init__(self):
        pass

    def dump(self,obj,fp):
        new_obj = to_ser(obj)
        with open(fp,'w') as json_file:
            json.dump(new_obj,json_file,indent=4)

    def dumps(self, obj):
        try:
            return json.dumps(to_ser(obj))
        except Exception:
            return None
            
    def load(self,fp):
        with open(fp,'r') as json_file:
            return from_ser(json.load(json_file))

    def loads(self,s):
        return (from_ser(json.loads(s)))