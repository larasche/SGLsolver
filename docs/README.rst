*********
SGLSOLVER
*********

Introduction
============

Package containing routines for solving the schrödinger equation for 
different potentials.

*****
Usage
*****

Input
=====

The following text shows an example how the .int data has to be structured

schrodinger.int

    2.0 # mass
    -2.0 2.0 1999 # xMin xMax nPoint
    1 5 # first and last eigenvalue to print
    linear # interpolation type
    2 # nr. of interpolation points and xy declarations
    -2.0 0.0
    2.0 0.0
	
Apllication
===========

Solvers
-------

./solvers.py -d [Directory]
	Solves the SGL for the given problem in the given Directory
	
Returns:

* energies.dat:	.dat containing energie and eigenvalues
		
* potential.dat:	.dat containing the interpolatet potential
		
* wavefunction.dat:	.dat containing the eigenvectors

Plotmain
--------
		
./plotmain.py -d [Directory ] -ymin [Ymin] -ymax [Ymax] -s [Scaling]
	Visualise the solved problem in a graph
	
Returns:

* graph.pdf:		.pdf containing graphs

************
Test Solvers
************

There are some test to test the Examplefiles