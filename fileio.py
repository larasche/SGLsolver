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
    indata["xMin"] = instring.split()[0]
    indata["xMax"] = instring.split()[1]
    indata["nPoint"] = instring.split()[2]
    instring = fp.readline()
    indata["firstEV"] = instring.split()[0]
    indata["lastEV"] = instring.split()[1]
    instring = fp.readline()
    indata["interpolationtype"] = instring.split()[0]
    instring = fp.readline()
    indata["nr_interpolation_points"] = instring.split()[0]
    fp.close

    fp = open(directory+"schrodinger.int", "r")
    aa = []
    for i, line in enumerate(fp):
        if i <= 4:
            continue
        elif i > 4:
            aa += line.split(" ")

    print(aa)

    indata["inter_points_x"] = aa[::2]
    indata["inter_points_y"] = aa[1::2]
    print(indata)



    return indata