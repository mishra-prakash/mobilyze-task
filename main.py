from extract.eurostat_api import EurostatAPI
from transform.dframes import Calculate, Curate
from load.load_to_csv import Load

def main():
    print("Inside Main")
    #### Initialising eurostat API
    estat = EurostatAPI()
    # Fetching all geo code and geo names mapping
    all_regions = estat.geoCodeNameMapping()

    # Filtering the above data only for Slovakia regions
    all_slovakia_regions = Curate.regionList(all_regions, country="SK") 
    print(all_slovakia_regions)

    #### Extracting Population data per 1 square km grid in Slovakia for 2006 and 2021
    data = estat.getData(all_slovakia_regions, start_time="2006", end_time="2021")
    print(data)
    
    #### Calcuating desired metrics by using Pandas
    task_1 = Calculate.first_task(data)
    task_2 = Calculate.second_task(data)
    print(task_1)
    print(task_2)
    #### Load the data
    Load.to_csv(task_1, name="first_assignment")
    Load.to_csv(task_2, name="second_assignment")

main()