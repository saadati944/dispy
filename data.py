import os
import config



slash='/'
if os.name=='nt':
    slash='\\'


def get_static_data(name):
    try:
        assert os.path.exists(config.static_data+slash+name)
        return open(config.static_data+slash+name,'r',encoding='utf-8').read()
    except:
        return f"can't find static data '{name}'"