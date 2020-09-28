"""Interpolates the potential from the indata
"""
import fileio
import numpy as np
import scipy.interpolate as sp
import scipy


def interpolation_pot(indata):
    """This function interpolates the potential linear, cubic or polynomial and
    writes the result in a file (potential.dat).

    Args.:
        indata: dictionary with the interpolation points and the x range.

    Returns.:
        int_potential: discretized potential in the x range
    """
    x_values = indata["inter_points_x"]
    y_values = indata["inter_points_y"]
    x_range = np.linspace(indata["xMin"], indata["xMax"], indata["nPoint"])
    if indata["interpolationtype"] == "linear":
        interpolation = sp.interp1d(x_values, y_values,
                                                kind="linear")
    elif indata["interpolationtype"] == "cspline":
        interpolation = sp.CubicSpline(x_values, y_values,
                                                bc_type = "natural")
    elif indata["interpolationtype"] == "polynomial":
        interpolation = np.poly1d(np.polyfit(x_values, y_values,
                                             indata["nr_interpolation_points"]
                                             - 1))
    int_potential = interpolation(x_range)

    fileio.write_int_pot(x_range, int_potential, indata["directory"])
    return int_potential

# delete the int_potential!!!!!!!!!!!!!:
def solve_EV_problem(indata, int_potential):
    """Solves the eigenvalue problem and returns the energies and wavefunctions.

    Args.:
        indata: dictionary with
        int_potential: discretized potential in the x range

    Returns.:
        energies: eigenenergies
        wavefunc: wavefunction
    """
    directory = indata["directory"]
    xrange, potential = fileio.read_int_pot(directory)
# distance of grid points
    delta = (abs(indata["xMax"]) + abs(indata["xMin"]))/indata["nPoint"]
# short
    a = 1/(indata["mass"] * delta**2)

# matrix elements:
    matrixdiagele = potential + a
    ndiag = np.ones(len(potential) - 1) * (-1/2) * a
    matrix = np.diag(matrixdiagele) + np.diag(ndiag, k=1) + np.diag(-ndiag,
                    k=-1)
    # print(matrix)
    energies, wavefct = scipy.linalg.eigh(matrix,
                                          eigvals=(indata["firstEV"] - 1,
                                          indata["lastEV"] - 1))

    print(energies)
    print(wavefct)
    fileio.write_energies(energies, directory)
    return
