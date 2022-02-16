from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations within 10 km of the Cambridge city centre
    numstations = rivers_by_station_number(stations, 9)
    print(numstations)



if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()