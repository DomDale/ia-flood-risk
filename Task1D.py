from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations within 10 km of the Cambridge city centre
    rivers = sorted(rivers_with_station(stations))
    print(len(rivers), "rivers. First 10", rivers[:10])

    # Print the names of stations located on specific rivers
    stationsbyriver = stations_by_river(stations)

    print("River Aire\n" + str(sorted([i.name for i in stationsbyriver["River Aire"]])))

    print("River Cam\n" + str(sorted([i.name for i in stationsbyriver["River Cam"]])))

    print("River Thames\n" + str(sorted([i.name for i in stationsbyriver["River Thames"]])))



if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()