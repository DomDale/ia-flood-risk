from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt
import datetime
import numpy as np

from floodsystem.plot import plot_water_level_with_fit, plot_water_levels


def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    levelsstations = stations_highest_rel_level(stations, 0) #return stations and relative water levels
    lowrisk, medrisk, highrisk, severerisk = [], [], [], []
    print(levelsstations)
    for i in levelsstations:
        if i[1]<-1:
            lowrisk+=[i]
        elif i[1]<0:
            medrisk+=[i]
        elif i[1]<1:
            highrisk+=[i]
        else:
            severerisk+=[i]

    print(len(lowrisk),len(medrisk),len(highrisk),len(severerisk))
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

