import eurostat
from transform.filters import Filter

class EurostatAPI():

    def __init__(self):
        ### Get dataset code for "Population density by NUTS 3 region"
        print("API initialised!")
        self.code = "DEMO_R_D3DENS"

    # Fetch geo code and names mapping   
    def geoCodeNameMapping(self): 
        geo_names = eurostat.get_dic(self.code, 'geo', full=False, frmt="dict", lang="en")
        return geo_names


    # Fetch Population data
    def getData(self, all_slovakia_regions,start_time, end_time):
        
        filtered_geo_names = all_slovakia_regions[0] 
        region_code_list = all_slovakia_regions[1]

        # Create Filter Params
        filter_params = Filter.create(region_code_list, start_time, end_time)
        
        # Make API call to fetch population data
        data = eurostat.get_data_df(self.code,flags=False, filter_pars=filter_params)
        
        return [data,filtered_geo_names,region_code_list]