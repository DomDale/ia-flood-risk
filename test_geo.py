"""Unit test for the geo module"""

import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def test_stations_by_distance():
    """Test when listing the stations by distance the first value is correct (cam)"""
    # Build list of stations
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    ordered = geo.stations_by_distance(stations, centre)
    assert ordered[0][0].name == "Cambridge Jesus Lock"


def test_stations_within_radius():
    """Test only the stations within Cambridge appear when queried"""
    # Build list of stations
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    searched = geo.stations_within_radius(stations, centre,5)
    assert len(searched) == 3

def test_rivers_with_station():
    """Test a few rivers that should exist do"""
    # Build list of stations
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    assert("Trout Beck" in rivers)
    assert("Ching Brook" in rivers)

def test_stations_by_river():
    """Test a few rivers that should exist do"""
    # Build list of stations
    stations = build_station_list()
    rivers = geo.stations_by_river(stations)
    assert(len(rivers["The Porter River"])==1)