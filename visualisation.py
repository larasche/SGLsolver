"""Visualisation of the engergies, the potential and the wave functions."""
import numpy as np
import matplotlib.pyplot as plt
import fileio


def graph(indata, ymin, ymax):
    """Creates a plot of wavefunctions for a potential,
        depending on different energies.
        Args:
            energies: eigenenergies
            potential: potentials
            wavefct: wavefunctions
            xrange: x values
            xmin: min. value of the x-axis
            xmax: max. value of the x-axis
            ymin: min. value of the y-axis
            ymax: max. value of the y-axis
        """
    xrange, potential = fileio.read_int_pot(indata["directory"])
    plt.plot(xrange, potential)
    energies = fileio.read_energies(indata["directory"])
    wavefct = fileio.read_wavefct(indata["directory"])
    plt.plot(xrange, wavefct + energies)
    plt.ylim(ymin, ymax)
    plt.xlim(indata["xMin"], indata["xMax"])

# horizontal line
    for ii in energies:
        plt.axhline(ii, indata["xMin"], indata["xMax"])

    return
