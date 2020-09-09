import os
import config



slash='/'
if os.name=='nt':
    slash='\\'



#this function return an array of lines !!!
def get_static_data(name, user=False):
    try:
        assert os.path.exists(config.static_data+slash+name)
        if not user:
            return open(config.static_data+slash+name,'r',encoding='utf-8').readlines()
        else :
            res=open(config.static_data+slash+name,'r',encoding='utf-8').readlines()
            assert len(res)>0 and not res[0].startswith('hidden')
            return res
    except:
        return [f"can't find static data '{name}'"]
