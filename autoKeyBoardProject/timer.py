import time as t
class Timer:
    def __init__(self,time):
        self.time=time
        self.begin=t.localtime
    
    def check(self):
        if t.localtime()-self.begin>self.time:
            return(True)
        else:
            return(False)