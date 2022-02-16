from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Getting list of stations and distance to city centre
    centre = (52.2053, 0.1218)
    sorteddistances = stations_by_distance(stations, centre)

    # Print a list of tuples for ten closest and furthest station
    closest = []
    furthest =  []
    for x in sorteddistances[:10]:
        closest.append((x[0].name, x[0].town, x[1]))
    for x in sorteddistances[-10:]:
        furthest.append((x[0].name, x[0].town, x[1]))

    print("Closest:", closest)
    print("Furthest:", furthest)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()