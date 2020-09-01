# UCSF Biophysics Bootcamp
# Ramachandran Project Assistance
# August 27, 2020

"""
This is an alternate method for generating Ramachandran plots
that uses the MDAnalysis package to calculate dihedral angles.
"""

# Import useful modules
import sys, re, math
import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis.dihedrals import Ramachandran

## 1. Read in PDB file
read_3emn = mda.Universe("/home/yessica/VDAC_project/bin/pdbs/3emn_noalt.pdb")

## 2. For every residue, extract the desired atoms with the corresponding Names
pol_atoms = read_3emn.select_atoms("protein")

## 4. Calculate the phi and psi angles
angles = Ramachandran(pol_atoms).run()

## 5. Make a scatter plot of phi and  psi values
fig, ax = plt.subplots(figsize=plt.figaspect(1))
angles.plot(ax=ax, color='k')
plt.show()
