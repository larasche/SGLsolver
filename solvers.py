"""Routines for solving a schrödinger equation"""
import fileio as io
import interpolation as inter
import visualisation as vi


def solver(directory="."):
    indata = io.read_schrodinger_inp(directory)
    inter.interpolation_pot(indata)
    inter.solve_EV_problem(indata)
    inter.calc_expected_value(indata)
    vi.graph(indata)
    return
