# -*- coding: utf-8 -*-
""""
Test's for pytest, to see if results match the reference data.

Author: Malte Kehlenbeck
"""
import warnings
import scipy
import numpy as np
import pytest
import fileio as fi
import interpolation as inp

warnings.simplefilter("always")

TESTNAMES = ['infinit_pot', 'finit_pot', 'harm_oscillator', 'asym_pot',
             'double_pot_lin', 'double_pot_cub']

@pytest.mark.parametrize("testname", TESTNAMES)
def test_pot(testname):
    """ Function to test potential

        Args:
            example: directory containing schroedinger.inp and
            ref_potential.dat

    """
    path = './examplefiles/' + testname + '/'
    # read ref pot
    ref_potential = np.loadtxt(path + 'ref_potential.dat')[:, 1]
    # calculate pot from schroedinger.inp
    aa = fi.read_schrodinger_inp(path)
    compare_pot = inp.interpolation_pot(aa)
    assert np.all(ref_potential - compare_pot < 1e-6)


@pytest.mark.parametrize("testname", TESTNAMES)
def test_ev(testname):
    """(Ugly)Function to test Eigenvalues

        Args:
            example: directory containing schroedinger.inp and ref_energies.dat
    """

    path = './examplefiles/' + testname + '/'
    # read ref energies
    ref_en = np.loadtxt(path + 'ref_energies.dat')
    # calculate ev from schroedinger.inp using placeholder as a var to store inputdata
    placeholder = fi.read_schrodinger_inp(path)
    # use part of interpolation.solve_ev to just calculate the energies
    directory = placeholder["directory"]
    xrange, potential = fi.read_int_pot(directory)
    # distance of grid points
    delta = (abs(aa["xMax"] - aa["xMin"])) / aa["nPoint"]
    # short
    ax = 1 / (aa["mass"] * delta ** 2)
    # matrix elements:
    matrixdiagele = potential + ax
    ndiag = np.ones(len(potential) - 1) * (-1 / 2) * ax
    matrix = np.diag(matrixdiagele) + np.diag(ndiag, k=1) + np.diag(ndiag,
                                                                    k=-1)
    energies, wavefct = scipy.linalg.eigh(matrix,
                                          eigvals=(aa["firstEV"] - 1,
                                                   aa["lastEV"] - 1))
    comp_en = np.transpose(np.array(energies))
    # comp_en = np.loadtxt(path + 'energies.dat')

    assert np.all(ref_en - comp_en < 1e-2)
