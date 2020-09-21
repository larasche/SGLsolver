"""Routines for solving a schrödinger equation"""
import numpy as np
import fileio
import interpolation

aa = fileio.read_schrodinger_inp("infinit_pot/")
pot = interpolation.interpolation_pot(aa)
print(pot)