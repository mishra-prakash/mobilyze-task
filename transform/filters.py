class Filter():
    def __init__(self):
        pass
    
    @staticmethod
    def create(region_list,start_time, end_time):
        return {   
            'geo': region_list,
            'startPeriod': start_time,
            'end_period': end_time
        }    

