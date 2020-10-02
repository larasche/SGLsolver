# -*- coding: utf-8 -*-
"""Main function to plot the energies, the potential, the wavefunction, the
expected value from the position operator and the uncertainty."""
import visualisation as vis
import fileio as io
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, required=True)
    parser.add_argument("-ymin ", "--yMin", type=float, required=True)
    parser.add_argument("-ymax", "--yMax", type=float, required=True)
    parser.add_argument("-s", "--scaling", type=float, required=True)
    args = parser.parse_args()
    print(args)
    indata = io.read_schrodinger_inp(args.directory)
    vis.graph(indata, args.yMin, args.yMax, args.scaling)

    return


if __name__ == '__main__':
    main()
