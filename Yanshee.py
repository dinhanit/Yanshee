import time
import YanAPI

class YanShee:
    def __init__(self,ip_addr):
        YanAPI.start_play_motion(name='reset')
        YanAPI.yan_api_init(ip_addr)
    def single_motion(self,name,direction='',speed='normal',repeat=1,timestamp=0):
        YanAPI.start_play_motion(name=name,direction=direction,speed=speed,repeat=repeat,timestamp=timestamp)
    def dance(self,name):
        YanAPI.start_play_motion(name=name)
    def multi_motion(self,dict_motion):
        keys=list(dict_motion.keys())
        for key in keys:
            inf_motion = dict_motion[key]
            YanAPI.start_play_motion(name=inf_motion['name'],direction=inf_motion['direction'],repeat=int(inf_motion['repeat']))
            time.sleep(1)
        
        
