# UCSF Biophysics Bootcamp
# Ramachandran Project Assistance
# July 21st, 2020

"""
As you start working on the ramachandran project, here is a helpful starting
template with names and descriptions of functions that will be useful
"""

# Import useful modules
import sys
import re
import math
import numpy as np
import matplotlib.pyplot as plt
# import requests

def add(vec_1, vec_2):
    """
    This function performs vector addition. This is a good place
    to play around with different collection types (list, tuple, set...),

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :return vec_3: a subscriptable collection of length 3
    """

    # add two vectors
    vec_3 = [float(vec_1[0]) + float(vec_2[0]), float(vec_1[1]) + float(vec_2[1]), float(vec_1[2]) + float(vec_2[2])]

    return vec_3

def subtract(vec_1, vec_2):
    """
    This function performs vector subtraction. This function should be
    almost identical to the add function.

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :return vec_3: a subscriptable collection of length 3
    """

    # subtract two vectors
    vec_3 = [float(vec_2[0]) - float(vec_1[0]), float(vec_2[1]) - float(vec_1[1]), float(vec_2[2]) - float(vec_1[2])]

    return vec_3

def normalize(vec):
    """
    From a length-3 vector return a normalized vector

    :param vec: a subscriptable collection of length 3
    :return norm_vec: a subscriptable collection
    """

    # Calculate the length of the vector
    vec_len = float(vec[0] + vec[1] + vec[2])
    # Divide the components of vec by the length of the vector
    norm_vec = [vec[0] / vec_len, vec[1] / vec_len, vec[2] / vec_len]

    return norm_vec

def dot(vec_1, vec_2):
    """
    From two vectors calculate and return the dot product. This
    is also know as the inner product and is scalar value (that represents
    the product of the magnitudes of the two vectors and the cosine of the
    angle between them).

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :return dot_product: scalar value (float)
    """

    # Using cartesian coordinates, calculate the dot product
    dot_product = vec_1[0] * vec_2[0] + vec_1[1] * vec_2[1] + vec_1[2] * vec_2[2]

    return dot_product

def cross(vec_1, vec_2):
    """
    From two vectors calculate and return the cross product. This is
    also known as the outer product and is a vector (that represents
    an orthogonal vector in 3-space).

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :return cross_product: a subscriptable collection of length 3
    """

    # Calculate the components of the cross-product vector
    cross_product_1 = vec_1[1] * vec_2[2] - vec_1[2] * vec_2[1]
    cross_product_2 = vec_1[2] * vec_2[0] - vec_1[0] * vec_2[2]
    cross_product_3 = vec_1[0] * vec_2[1] - vec_1[1] * vec_2[0]

    cross_product = [cross_product_1, cross_product_2, cross_product_3]

    return cross_product

def calc_torsion(vec_1, vec_2, vec_3, vec_4):
    """
    Using four sequential vectors in cartesian space, each representing
    a position of an atom, the torsion between vec_2 and vec_3 is calculated.

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :param vec_3: a subscriptable collection of length 3
    :param vec_4: a subscriptable collection of length 3
    :return tor: a scalar value of the torsion
    """

    # Create vectors between the four atoms
    line_1 = subtract(vec_1, vec_2)
    line_2 = subtract(vec_3, vec_2)
    line_3 = subtract(vec_4, vec_3)

    # Normal vectors between two intersecting planes created by new vectors
    plane_1 = normalize(cross(line_1, line_2))
    plane_2 = normalize(cross(line_2, line_3))

    # Calculate dihedral angle between two planes
    x = math.sqrt( math.pow(plane_1[0],2) + math.pow(plane_1[1],2) + math.pow(plane_1[2],2) )
    y = math.sqrt( math.pow(plane_2[0],2) + math.pow(plane_2[1],2) + math.pow(plane_2[2],2) )
    di_angle = math.acos(dot(plane_1, plane_2) / (x * y))

    return di_angle

def read_pdb(filename):
    """
    From a given path to a pdb file, return a list of lines containing
    atom data

    :param filename: directory to pdb file
    :return: suscriptable collection of atom data
    """

    # Read in file
    with open(filename,'r') as f:

        # Read lines from file
        flines = []
        for lines in f:
            flines.append(lines)

    # Close file (be kind rewind)

    # Initiate suscriptable collection to store atom data
    atom_data = []

    # Iterate over line data
    for line in flines:

        # Split the lines
        if "ATOM " in line:
            atom_data.append(line.split())

    # print (len(atom_data), atom_data[-1])

    # Return subscriptable collection
    return atom_data


## 1. Read in PDB file
read_3emn = read_pdb("/home/yessica/VDAC_project/bin/pdbs/3emn.pdb")

## 2. For every residue, extract the desired atoms with the corresponding Names
res_ignore = ['PRO', 'GLY']
vn_list = []
va_list = []
vc_list = []

for dp in read_3emn:

    if dp[3] not in res_ignore:

        ## 3. For this subset of atoms, assign atom coordinates from columns 6-8 to vectors
        if dp[2] == 'N':
            vn_list.append([dp[6],dp[7],dp[8]])
        elif dp[2] == 'CA':
            va_list.append([dp[6],dp[7],dp[8]])
        elif dp[2] == 'C':
            vc_list.append([dp[6],dp[7],dp[8]])
        else:
            pass

## 4. Using these atom vectors, calculate the phi angle, then the psi angle
phi_angles = []
psi_angles = []

print (len(vn_list), len(va_list), len(vc_list))
for j in range (len(vn_list)-1):
    phi_angles.append(math.pi - calc_torsion(vc_list[j], vn_list[j], va_list[j+1], vc_list[j+1]))
    psi_angles.append(math.pi - calc_torsion(vn_list[j+1], vc_list[j+1], va_list[j+1], vn_list[j]))

print(len(phi_angles), len(psi_angles), phi_angles[-1], psi_angles[-1])

## 5. Make a scatter plot of phi and  psi values
