#!/usr/bin/env python3
"""Routines for solving a schrodinger equation"""
import argparse
import fileio as io
import interpolation as inter


def main():
    """Main function to solve the schrodinger equation for a given potential
    """
    descr = "Program to solve the schrodinger equation"
    parser = argparse.ArgumentParser(description=descr)
    msg = "Directory in wich the file schrodinger.inp is stored"
    parser.add_argument("-d", "--directory", type=str, required=True, help=msg)
    args = parser.parse_args()

    indata = io.read_schrodinger_inp(args.directory)
    inter.interpolation_pot(indata)
    inter.solve_evproblem(indata)
    inter.calc_expected_value(indata)
    return


if __name__ == '__main__':
    main()
