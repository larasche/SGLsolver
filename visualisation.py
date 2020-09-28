"""Visualisation of the engergies, the potential and the wave function."""
import numpy as np
import matplotlib.pyplot as plt
import fileio


def graph(indata):
    """Creates a plot of wavefunctions for a potential,
        depending on different energies.
        Args:
            energies: eigenenergies
            discrpot: potentials
            wafef: wafefunctions
            xrange: x values
            xmin: min. value of the x-axis
            xmax: max. value of the x-axis
            ymin: min. value of the y-axis
            ymax: max. value of the y-axis
        """
    xrange, potential = fileio.read_int_pot(indata["directory"])
    plt.plot(xrange, potential)
 #   plt.plot(xrange, wavef + energies)
  #  plt.ylim(ymin, ymax)
   # plt.xlim(xmin, xmax)

# horizontal line
    #for ii in energies:
     #   plt.axhline(ii, -2, 2)

    return
