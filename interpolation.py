"""Interpolates the potential from the indata and calculates the energies and
normalized wavefunctions
"""
import numpy as np
import scipy.interpolate as sp
import scipy
import fileio


def interpolation_pot(indata):
    """This function interpolates the potential linear, cubic or polynomial.

    Args.:
        indata: dictionary with the directory, the interpolation points, the x
        range and the interpolation type.

    Returns:
        int_potential: discretized potential in the x range
    """
    x_values = indata["inter_points_x"]
    y_values = indata["inter_points_y"]
    x_range = np.linspace(indata["xMin"], indata["xMax"],
                          int(indata["nPoint"]))
    if indata["interpolationtype"] == "linear":
        interpolation = sp.interp1d(x_values, y_values,
                                    kind="linear")
    elif indata["interpolationtype"] == "cspline":
        interpolation = sp.CubicSpline(x_values, y_values,
                                       bc_type="natural")
    elif indata["interpolationtype"] == "polynomial":
        interpolation = np.poly1d(np.polyfit(x_values, y_values,
                                             indata["nr_interpolation_points"]
                                             - 1))
    int_potential = interpolation(x_range)

    fileio.write_int_pot(x_range, int_potential, indata["directory"])
    return int_potential


def solve_evproblem(indata):
    """Solves the eigenvalue problem and returns the energies and wavefunctions.

    Args.:
        indata: dictionary with the mass, the directory, the min and max x
                range, the number of x values and the first and last
                eigenvalues.

    Returns:
        energies: eigenenergies
        wavefunc: wavefunctions
    """
    directory = indata["directory"]
    xrange, potential = fileio.read_int_pot(directory)
# distance of grid points
    delta = (abs(indata["xMax"] - indata["xMin"]))/indata["nPoint"]
# short
    abbreviation = 1/(indata["mass"] * delta**2)

# matrix elements:
    matrixdiagele = potential + abbreviation
    ndiag = np.ones(len(potential) - 1) * (-1/2) * abbreviation
    matrix = np.diag(matrixdiagele) + np.diag(ndiag, k=1) + np.diag(ndiag,
                                                                    k=-1)
    energies, wavefct = scipy.linalg.eigh(matrix,
                                          eigvals=(indata["firstEV"] - 1,
                                                   indata["lastEV"] - 1))
    fileio.write_energies(energies, directory)
# norm the eigenfunctions:
    columns = len(wavefct[1])
    for ii in range(columns):
        psisquare = delta * np.sum(np.abs(wavefct[:, ii]) ** 2)
        wavefct[:, ii] = wavefct[:, ii]/(np.sqrt(psisquare))

    fileio.write_wavefct(wavefct, xrange, directory)
    return


def calc_expected_value(indata):
    """Calculates the expected value of the position operator and the
    uncertainty of the location measurement.

    Args.:
        indata: dictionary with with the name of the directory, min and max
                x values and the number of x points.

    """
    delta = (abs(indata["xMax"] - indata["xMin"]))/indata["nPoint"]
    xrange, wavefct = fileio.read_wavefct(indata["directory"])
    newxrange = np.linspace(indata["xMin"], indata["xMax"], indata["nPoint"])
    columns = len(wavefct[1])
# expected value from the position operator:
    exposval = np.zeros(columns)
    for ii in range(columns):
        exposval[ii] = delta * (np.sum(newxrange * wavefct[:, ii]**2))

# expectes value from the squared position operator:
    expvalsq = np.zeros(columns)
    for ii in range(columns):
        expvalsq[ii] = delta * (np.sum(newxrange ** 2 * wavefct[:, ii]**2))

# uncertainty of the location measurement:
    sigma = np.zeros(len(exposval))
    for ii in range(len(exposval)):
        sigma[ii] = np.sqrt(expvalsq[ii] - exposval[ii]**2)

    fileio.write_expvalues(exposval, sigma, indata["directory"])

    return
