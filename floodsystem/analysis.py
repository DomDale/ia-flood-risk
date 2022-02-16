"""This module contains a collection of functions related to
analysis.
"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    "implement a function that given the water level time history (dates, levels) for a station computes a least-squares fit of a polynomial of degree p to water level data"

    x = matplotlib.dates.date2num(dates)
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return poly, x[0]