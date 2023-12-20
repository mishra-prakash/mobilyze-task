import pandas as pd
import re
from extract.geopy_api import Locations

class Calculate():
    def __init__(self):
        pass
    
    @staticmethod
    def first_task(data_2006, data_2021):
        
        # get Latitude and Longitude by passing region_code_list
        geo_locations = Locations.getInfo(data_2006[2])
        
        
        region_name_mapping = data_2006[1]
        df06 = data_2006[0]
        df21 = data_2021[0]
        # Merge data for 2006 and 2021 based on the 'geo\TIME_PERIOD' column
        merged_data = pd.merge(df06, df21, on='geo\TIME_PERIOD')

        # Calculate relative increase in population
        merged_data['relative_change'] = (merged_data['2021'] - merged_data['2006']) / merged_data['2006'] * 100

        # Sort by relative increase in descending order
        sorted_data = merged_data.sort_values(by='relative_change', ascending=False)

        # Get the top 5 grid cells with the highest relative increase in population in Slovakia
        top_5_cells = sorted_data.head(5)

        #Adding geo_name to the top_5_cells dataframe
        top_5_cells['geo_name'] = top_5_cells['geo\TIME_PERIOD'].map(region_name_mapping)
        
        #Left joining top_5_cells dataframe with geo_locations dataframe to get Latitude and Longitude
        final_df = pd.merge(top_5_cells, geo_locations, on='geo\TIME_PERIOD', how='left')

        return final_df
    
    @staticmethod
    def second_task(df):
        avg = df["2021"].mean()
        median = df["2021"].median()
        return pd.DataFrame([avg,median],columns=['Average population per 1 sq km', ' Median population per 1 sq km'])



class Curate():
    def __init__(self):
        pass
    
    @staticmethod
    def regionList(geo_names, country=None):
        
        if geo_names and country:
            # filter Slovakia regions
            # All Slovakia region follows this pattern SK0**
            try:
                pattern = re.compile(r'SK0\d{2}')
                filtered_geo_names = {key: value for key, value in geo_names.items() if re.fullmatch(pattern, key)}
            
                # get region name list
                region_code_list = [key for key,value in filtered_geo_names.items()]
            
                return [filtered_geo_names,region_code_list]
            except Exception as e:
                print(f"Got this error{e.message}")
        else:
            print("Can't fetch curated region list. Please check arguments")
            return 403