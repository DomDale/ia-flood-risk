from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations within 10 km of the Cambridge city centre
    r = 10
    centre = (52.2053, 0.1218)
    withinradius = stations_within_radius(stations, centre, r) 
    names = sorted([i.name for i in withinradius])
    print(names)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()