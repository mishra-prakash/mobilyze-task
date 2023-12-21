from extract.eurostat_api import EurostatAPI
from transform.dframes import Calculate, Curate
from load.load_to_csv import Load

def main():

    #### Initialising eurostat API
    estat = EurostatAPI()

    # Fetch Dataset Code for Population density by NUTS 3 region.
    code = estat.getDatasetCode("Population density by NUTS 3 region")

    # Fetching all geo code and geo names mapping
    all_regions = estat.geoCodeNameMapping(code)

    # Filtering the above data only for Slovakia regions
    all_slovakia_regions = Curate.regionList(all_regions, country="SK") 

    #### Extracting Population data per 1 square km grid in Slovakia from 2006 to 2021
    data = estat.getData(code, all_slovakia_regions, start_time="2006", end_time="2021")

    
    #-------------------Task 1----------------------#
    #### Evaluating first task and loading it to csv
    task_1 = Calculate.first_task(data)
    Load.to_csv(task_1, name="first_assignment")
    

    #-------------------Task 2-----------------------#
    #### Evaluating second task and loading it to csv
    task_2 = Calculate.second_task(data)
    Load.to_csv(task_2, name="second_assignment")



if __name__ == "__main__":
    main()