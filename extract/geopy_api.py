from geopy.geocoders import Nominatim
import pandas as pd

class Locations():
    def __init__(self):
        pass

    def getInfo(region_code_list):
        geolocator = Nominatim(user_agent="tutorial")
        arr = []
        for i in region_code_list:
            location = geolocator.geocode(i)
            if location:
                latitude =location.latitude
                longitude= location.longitude
                arr.append([i, latitude, longitude])
        
        df = pd.DataFrame(arr,columns=['geo\TIME_PERIOD','latitude','longitude'])
        return df