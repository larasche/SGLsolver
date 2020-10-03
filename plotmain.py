# -*- coding: utf-8 -*-
"""Main function to plot the energies, the potential, the wavefunction, the
expected value from the position operator and the uncertainty."""
import argparse
import visualisation as vis
import fileio as io


def main():
    """Main function to plot the data
    """
    descr = "Function to plot the solutions from the solvers module"
    parser = argparse.ArgumentParser(description=descr)
    msg = "Directory in wich the file schrodinger.inp is stored"
    parser.add_argument("-d", "--directory", type=str, required=True, help=msg)
    msg = "Minimum y value for the plot of the wavefunctions"
    parser.add_argument("-ymin ", "--yMin", type=float, required=True,
                        help=msg)
    msg = "Maximum y value for the plot of the wavefunctions"
    parser.add_argument("-ymax", "--yMax", type=float, required=True, help=msg)
    msg = "Scaling factor for the wavefunction"
    parser.add_argument("-s", "--scaling", type=float, required=True, help=msg)
    args = parser.parse_args()
    indata = io.read_schrodinger_inp(args.directory)
    vis.graph(indata, args.yMin, args.yMax, args.scaling)

    return


if __name__ == '__main__':
    main()
