"""Visualisation of the engergies, the potential and the wave functions."""
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
    energies = fileio.read_energies(indata["directory"])
    xrange, wavefct = fileio.read_wavefct(indata["directory"])
    expval, sigma = fileio.read_expvalues(indata["directory"])

    plt.subplot(121)
    # horizontal line
    for ii in energies:
        plt.axhline(ii, indata["xMin"], indata["xMax"], color="lightgrey")

    plt.plot(xrange, potential)
    plt.plot(xrange, wavefct*0.2 + energies)
    plt.plot(expval, energies, "x", color="forestgreen")

    plt.ylim(ymin, ymax)
    plt.xlim(indata["xMin"], indata["xMax"])

    plt.title("Potential, eigenstates, ⟨x⟩")
    plt.ylabel("Energy [Hartree]")
    plt.xlabel("x [Bohr]")


# plot the uncertainty:
    plt.subplot(122)

    plt.xlim(0, indata["xMax"])
    plt.ylim(ymin, ymax)

    for ii in energies:
        plt.axhline(ii, indata["xMin"], indata["xMax"], color="lightgrey")

    plt.plot(sigma, energies, "+m", markersize=10)

    plt.title("σₓ")
    plt.xlabel("[Bohr]")

    plt.savefig(indata["directory"]+"graph.pdf")
    return
