"""Visualisation of the engergies, the potential and the wave functions."""
import numpy as np
import matplotlib.pyplot as plt
import fileio


def graph(indata, ymin, ymax, scaling):
    """Creates a plot of wavefunctions for a potential,
        depending on different energies.
        Args:
            indata: dictionary with the directory, the min x values and the max
                    x values
            ymin: min. value of the y-axis
            ymax: max. value of the y-axis
            scaling: scaling factor for the wavefunction
        """
    xrange, potential = fileio.read_int_pot(indata["directory"])
    energies = fileio.read_energies(indata["directory"])
    xrange, wavefct = fileio.read_wavefct(indata["directory"])
    expval, sigma = fileio.read_expvalues(indata["directory"])
# plot the energies, wavefunctions and expected values
    plt.subplot(121)

    for ii in energies:
        plt.axhline(ii, indata["xMin"], indata["xMax"], color="lightgrey")

    plt.plot(xrange, potential, color="black")

    rows, columns = wavefct.shape
    for ii in range(columns):
        if ii % 2:
            plt.plot(xrange, wavefct[:, ii]*scaling + energies[ii],
                     color="red")
        else:
            plt.plot(xrange, wavefct[:, ii]*scaling + energies[ii],
                     color="blue")

    plt.plot(expval, energies, "x", color="forestgreen")

    plt.ylim(ymin, ymax)
    plt.xlim(indata["xMin"], indata["xMax"])

    plt.title("Potential, eigenstates, ⟨x⟩")
    plt.ylabel("Energy [Hartree]")
    plt.xlabel("x [Bohr]")


# plot the uncertainty:
    plt.subplot(122)
    xMax = np.max(sigma)
    xmaxplot = xMax + xMax * 0.2
    plt.xlim(0, xmaxplot)
    plt.ylim(ymin, ymax)

    for ii in energies:
        plt.axhline(ii, indata["xMin"], indata["xMax"], color="lightgrey")

    plt.plot(sigma, energies, "+m", markersize=10)

    plt.title("σₓ")
    plt.xlabel("[Bohr]")

    plt.savefig(indata["directory"]+"graph.pdf")
    return
