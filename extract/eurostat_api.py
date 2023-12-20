import eurostat
from transform.filters import Filter

class EurostatAPI():

    def __init__(self):
        ### Get dataset code : We are interested in - "Population density by NUTS 3 region"
        self.code = "DEMO_R_D3DENS"
        
    def geoCodeNameMapping(self): 
        print(self.code)
        geo_names = eurostat.get_dic(self.code, 'geo', full=False, frmt="dict", lang="en")
        print(geo_names)
        return geo_names


    # Fetch data for 2006
    def getData(self, all_slovakia_regions,start_time, end_time):
        
        filtered_geo_names = all_slovakia_regions[0] 
        region_code_list = all_slovakia_regions[1]

        # Create Filter Params
        filter_params = Filter.create(region_code_list, start_time, end_time)
        print(filter_params)
        data = eurostat.get_data_df(self.code,flags=False, filter_pars=filter_params)
        
        return [data,filtered_geo_names,region_code_list]