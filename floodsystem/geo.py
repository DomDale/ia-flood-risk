# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from math import dist
from .utils import sorted_by_key  # noqa
from geopy import distance

def stations_by_distance(stations, p):
    """Passed a list of station objects and a co-ordinate, returns station objects, closest to farthest."""
    distances = []
    for n in stations:
        distances.append((n, distance.distance(p, n.coord).km))
    sorteddistances = sorted_by_key(distances, 1)
    return sorteddistances

def stations_within_radius(stations, centre, r):
    """Passed a list of station objects, a centre co-ord and a radius in km; returns stationobjects within that radius"""
    withinradius = []
    for n in stations:
        dist = distance.distance(centre, n.coord).km
        if dist < r:
            withinradius.append(n)
    return withinradius
        

def rivers_with_station(stations):
    """Passed a list of station objects, returns a dict of all the rivers the stations are on. Repeats are ignored (dict)"""
    return {n.river for n in stations}

def stations_by_river(stations):
    """Passed a list of station objects, returns a dict of rivers as a key a list of stations as their value"""
    riverstations = {}
    rivers = rivers_with_station(stations)
    for n in stations:
        if n.river in riverstations:
            riverstations[n.river].append(n)
        else:
            riverstations[n.river] = [n]
    return riverstations

def rivers_by_station_number(stations, N):
    """Passed a list of station objects and a number N, returns the list of N river objects from with the most monitoring stations on it."""
    riverstation = stations_by_river(stations)
    numstations = sorted_by_key([(i, len(riverstation[i])) for i in riverstation], 1, reverse=True)

    cutoff = numstations[N-1][1] #we want to return the top N stations but also include any more than N if they have the same number as a value which would be included 
    numstationsreduced = []
    for i in numstations:
        if i[1] >= cutoff:
           numstationsreduced.append(i)
    return numstationsreduced
        
