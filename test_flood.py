"""Unit tests for the flood module"""

import floodsystem.flood
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_stations_highest_rel_level():    
    stations = build_station_list()
    update_water_levels(stations)
    topstations = stations_highest_rel_level(stations, 5)
    prevval = -10000
    for i in topstations:
        assert i[1] > prevval
        prevval = i[1]
