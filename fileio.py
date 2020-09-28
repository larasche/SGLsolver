#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 16:19:57 2020

@author: larasche
"""

"""File Io for the sglsolver module"""
import numpy as np


def read_schrodinger_inp(directory="."):
    """Read the data input file and creates a Dictionarie with the data

    Args.:
        directory: The directory with the schrodinger.int file

    Returns.:
        indata: Dictionarie with the data from the input file
    """
    fp = open(directory+"schrodinger.int", "r")
    indata = {}
    indata["directory"] = directory
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
    fp.close
# reads the interpolation points:
    fp = open(directory+"schrodinger.int", "r")
    aa = []
    for i, line in enumerate(fp):
        if i <= 4:
            continue
        elif i > 4:
            aa += line.split(" ")

    aa = list(map(float, aa))

    indata["inter_points_x"] = np.array(aa[::2])
    indata["inter_points_y"] = np.array(aa[1::2])
    print(indata)
    return indata


def write_int_pot(x_range, int_potential, directory):
    """Writes the calculated potential and the x values in a file (x, V(X))

    Args.:
        x_range: xvalues
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
    fp = open(directory+"potential.dat", "r")
    aa = []
    for i, line in enumerate(fp):
        aa += line.split(" ")
    aa = list(map(float, aa))
    xrange = np.array(aa[::2])
    potential = np.array(aa[1::2])
#    print(xrange)
#    print(potential)
    return xrange, potential


def write_energies(energies, directory):
    """Writes the energies in the file energies.dat in the directory with the
    given potential.

    Args.:
        energies: calculated energies
        directory: directory in which the file have to be saved
    """
    energies = np.transpose(np.array(energies))
    np.savetxt(directory+"energies.dat", energies)


def read_energies(directory):
    """Reads the calculated energies from the file energies.dat from a
    directory.

    Args.:
        directory: directory in which the file with the energies are saved

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
        x_range: x range
        wavefct: calculated wavefunction
    """
   # print(xrange.shape, wavefct.shape)
    xrange = np.reshape(xrange, (len(xrange), 1))
    xrange_wavefct = np.concatenate((xrange, wavefct), axis=1)
    np.savetxt(directory+"wavefuncs.dat", xrange_wavefct)


def read_wavefct(directory):
    fp = open(directory+"wavefuncs.dat", "r")
