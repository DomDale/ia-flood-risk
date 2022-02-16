from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Outputs a list of station names from the dataset with inconsistent data"""

    # Build list of stations
    stations = build_station_list()
    # Get ones with inconsidstent data
    inconsistent = inconsistent_typical_range_stations(stations)
    print(inconsistent)
    print(sorted([i.name for i in inconsistent]))


if __name__ == "__main__":
    print("*** Task 1G: CUED Part IA Flood Warning System ***")
    run()