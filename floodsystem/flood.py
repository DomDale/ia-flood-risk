"""This module contains a collection of functions related to
flood data.
"""
from floodsystem.utils import sorted_by_key
from floodsystem.station import relative_water_level


def stations_level_over_threshold(stations, tol):
    "Returns stations that have rel water level over threshold in order"
    overthresh = []
    for i in stations:
        if (i.relative_water_level() is not None) and (i.relative_water_level() > tol):
            overthresh.append((i, i.relative_water_level() - tol))
    sortedover = sorted_by_key(overthresh, 1)
    return sortedover
            

def stations_highest_rel_level(stations, N):
    "returns list of N stations at which water level relative to typical range is highest"
    stationlevels = [(i, i.relative_water_level) for i in stations]
    sortedstationlevels = sorted_by_key(stationlevels, 1)
    return sortedstationlevels[:10]
