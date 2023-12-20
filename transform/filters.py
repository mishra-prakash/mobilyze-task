class Filter():
    def __init__(self):
        pass
    
    @staticmethod
    def create(region_list,time):
        return {   
            'geo': region_list,
            'startPeriod': time,
            'end_period': time
        }    

