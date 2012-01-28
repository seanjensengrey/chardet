import os.path as p

try:
    import simplejson as json
except ImportError:
    import json


def read_freq_table(fp,key):
    o = json.loads(open(p.join(p.split(__file__)[0],fp)).read())
    return o[key]


def write_freq_table(fp,key,data):
    f = open(fp,'w')
    o = {}
    o[key] = data
    f.write(json.dumps(o))
    f.close()
