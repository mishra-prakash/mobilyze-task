import eurostat
from transform.filters import Filter

class EurostatAPI():

    def __init__(self):
        ### Get dataset code : We are interested in - "Population density by NUTS 3 region"
        self.code = "DEMO_R_D3DENS"
        
    def geoCodeNameMapping(self): 
        geo_names = eurostat.get_dic(self.code, 'geo', full=False, frmt="dict", lang="en")
        return geo_names


    # Fetch data for 2006
    def getData(self, all_slovakia_regions,time=None):
        
        filtered_geo_names = all_slovakia_regions[0] 
        region_code_list = all_slovakia_regions[1]

        # Create Filter Params
        filter_params = Filter.create(region_code_list, time)
        
        data = eurostat.get_data_df(self.code,flags=False, filter_pars=filter_params)
        
        return [data,filtered_geo_names,region_code_list]