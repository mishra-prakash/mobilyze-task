import pandas as pd
import re
from extract.geopy_api import Locations

class Calculate():
    def __init__(self):
        pass
    
    @staticmethod
    def first_task(data):
        
        # get Latitude and Longitude by passing region_code_list
        geo_locations = Locations.getInfo(data[2])
        
        region_name_mapping = data[1]
        df = data[0]

        # Calculate relative increase in population
        df['perc_relative_change'] = (df['2021'] - df['2006']) / df['2006'] * 100

        # Sort by relative increase in descending order
        sorted_data = df.sort_values(by='perc_relative_change', ascending=False)

        # Get the top 5 grid cells with the highest relative increase in population in Slovakia
        top_5_cells = sorted_data.head(5)

        #Adding geo_name to the top_5_cells dataframe
        top_5_cells['geo_name'] = top_5_cells['geo\TIME_PERIOD'].map(region_name_mapping)
        
        #Left joining top_5_cells dataframe with geo_locations dataframe to get Latitude and Longitude
        final_df = pd.merge(top_5_cells, geo_locations, on='geo\TIME_PERIOD', how='left')
        final_df.rename(columns={'2006': 'population_per_sq_km_2006', '2021': 'population_per_sq_km_2021','geo\TIME_PERIOD': 'geo_code'}, inplace=True)
        final_df['perc_relative_change'] = final_df['perc_relative_change'].round(2).astype(str) + '%'
        
        f_df = final_df[['geo_code','geo_name','latitude', 'longitude', 'population_per_sq_km_2006', 'population_per_sq_km_2021', 'perc_relative_change']]
        print("----------------- {This  is output of task 1} --------------------")
        print(f_df)
        
        return f_df
    
   
    @staticmethod
    def second_task(data):
        df = data[0]

        avg = df['2021'].mean().round(2)
        median = df['2021'].median().round(2)
        
        final_df = pd.DataFrame([[avg,median]],columns=['Average population per 1 sq km', ' Median population per 1 sq km'])
        print("----------------- {This  is output of task 2} --------------------")
        print(final_df)
        
        return final_df



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