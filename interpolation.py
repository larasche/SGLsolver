"""Interpolates the potential from the indata
"""
import fileio
import numpy as np
import scipy as sp


def interpolation_pot(indata):
    """This function interpolates the potential linear, cubic or polynomial.

    Args.:
        indata: dictionary withe the interpolation points and the x range.

    Returns.:
        int_potential: discretized potential in the x range
    """
    x_values = indata["inter_points_x"]
    y_values = indata["inter_points_y"]
    x_range = np.linspace(indata["xMin"], indata["xMax"], indata["nPoint"])
    if indata["interpolationtype"] == "linear":
        interpolation = sp.interpolate.interp1d(x_values, y_values,
                                                kind="linear")
    elif indata["interpolationtype"] == "cspline":
        interpolation = sp.interpolate.interp1d(x_values, y_values,
                                                kind="cubic")
    elif indata["interpolationtype"] == "polynomial":
        interpolation = np.poly1d(np.polyfit(x_values, y_values,
                                             indata["nr_interpolation_points"]
                                             - 1))
    int_potential = interpolation(x_range)
    return int_potential