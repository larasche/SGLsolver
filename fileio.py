#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""File Io for the sglsolver module"""
import numpy as np


def read_schrodinger_inp(directory):
    """Read the data input file and creates a Dictionarie with the data

    Args.:
        directory: The directory with the schrodinger.int file

    Returns.:
        indata: Dictionarie with the data from the input file
    """
    with open(directory+"schrodinger.int", "r") as fp:
        indata = {"directory": directory}
        instring = fp.readline()
        indata["mass"] = float(instring.split()[0])
        instring = fp.readline()
        indata["xMin"] = float(instring.split()[0])
        indata["xMax"] = float(instring.split()[1])
        indata["nPoint"] = float(instring.split()[2])
        instring = fp.readline()
        indata["firstEV"] = int(instring.split()[0])
        indata["lastEV"] = int(instring.split()[1])
        instring = fp.readline()
        indata["interpolationtype"] = instring.split()[0]
        instring = fp.readline()
        indata["nr_interpolation_points"] = int(instring.split()[0])
    # reads the interpolation points:
    with open(directory+"schrodinger.int", "r") as fp:
        aa = []
        for i, line in enumerate(fp):
            if i <= 4:
                continue
            elif i > 4:
                aa += line.split(" ")

        aa = list(map(float, aa))

        indata["inter_points_x"] = np.array(aa[::2])
        indata["inter_points_y"] = np.array(aa[1::2])

        return indata


def write_int_pot(x_range, int_potential, directory):
    """Writes the calculated potential and the x values in the file
    potential.dat

    Args.:
        x_range: x values
        int_potential: discretized potential in the x range
        directory: directory to save the file potential.dat
    """
    aa = np.transpose(x_range)
    bb = np.transpose(int_potential)
    xrangeandpot = np.transpose(np.array([aa, bb]))
    np.savetxt(directory+"potential.dat", xrangeandpot)


def read_int_pot(directory):
    """Reads the x range and the potential from the file potential.dat

    Args.:
        directory: directory with the file potential.dat

    Returns.:
        xrange: x values
        potential: V(x)
    """
    with open(directory+"potential.dat", "r") as fp:
        aa = []
        for i, line in enumerate(fp):
            aa += line.split(" ")
        aa = list(map(float, aa))
        xrange = np.array(aa[::2])
        potential = np.array(aa[1::2])
        return xrange, potential


def write_energies(energies, directory):
    """Writes the energies in the file energies.dat in the directory with the
    given potential.

    Args.:
        energies: calculated energies
        directory: directory in which the file have to be stored
    """
    energies = np.transpose(np.array(energies))
    np.savetxt(directory+"energies.dat", energies)


def read_energies(directory):
    """Reads the calculated energies from the file energies.dat from a given
    directory.

    Args.:
        directory: directory in which the file with the energies are stored

    Returns:
        energies: calculated energies
    """
    fp = open(directory+"energies.dat", "r")
    energies = fp.readlines()
    energies = list(map(float, energies))
    return energies


def write_wavefct(wavefct, xrange, directory):
    """ Writes the wavefunctions and the x range in a file in the directory
    with the given potential

    Args.:
        x_range: x values
        wavefct: calculated wavefunction
        directory: directory in which the file have to be saved
    """
    xrange = np.reshape(xrange, (len(xrange), 1))
    xrange_wavefct = np.concatenate((xrange, wavefct), axis=1)
    np.savetxt(directory+"wavefuncs.dat", xrange_wavefct)


def read_wavefct(directory):
    """Reads the wavefunctions from the file wavefuncs.dat

    Args.:
        directory: directory in which the file with the wavefunctions are saved

    Returns:
        xrange: x values
        wavefct: array with the wavefunctions
    """
    data = np.loadtxt(directory+"wavefuncs.dat")
    column = len(data[1])
    xrange = data[:, 0]
    wavefct = data[:, 1:column]
    return xrange, wavefct


def write_expvalues(exposval, sigma, directory):
    """Writes the expected value of the poition operator and the uncertainty of
    the location measurement in the file expvalues.dat.

    Args.:
        exposval: expected value of the poition operator
        sigma: uncertainty of the location measurement
        directory: directory in which the file have to be saved
    """
    exposval = np.reshape(exposval, (len(exposval), 1))
    sigma = np.reshape(sigma, (len(sigma), 1))
    exposval_sigma = np.concatenate((exposval, sigma), axis=1)
    np.savetxt(directory+"expvalues.dat", exposval_sigma)

    return


def read_expvalues(directory):
    """Reads the expected value of the position operator and the uncertainty of
    the lacation measurement from the file expvalues.

    Args.:
        directory: directory in which the file with the values are saved

    Returns:
        exposval: expected value of the poition operator
        sigma: uncertainty of the location measurement
    """
    exposval_sigma = np.loadtxt(directory+"expvalues.dat")
    exposval = exposval_sigma[:, 0]
    sigma = exposval_sigma[:, 1]

    return exposval, sigma
