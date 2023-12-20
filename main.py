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
    data_2006 = estat.getData(all_slovakia_regions, time="2006")
    data_2021 = estat.getData(all_slovakia_regions, time="2021")

    #### Calcuating desired metrics by using Pandas
    task_1 = Calculate.first_task(data_2006, data_2021)
    task_2 = Calculate.second_task(data_2021)

    #### Load the data
    Load.to_csv(task_1, name="first_assignment")
    Load.to_csv(task_2, name="second_assignment")

main()