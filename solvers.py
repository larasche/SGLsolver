#!/usr/bin/env python3
"""Routines for solving a schrödinger equation"""
import fileio as io
import interpolation as inter
import visualisation as vi
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, required=True)
    args = parser.parse_args()

    indata = io.read_schrodinger_inp(args.directory)
    inter.interpolation_pot(indata)
    inter.solve_EV_problem(indata)
    inter.calc_expected_value(indata)
    #vi.graph(indata)
    return

if __name__ == '__main__':
    main()
