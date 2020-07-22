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
import requests

def add(vec_1, vec_2):
    """
    This function performs vector addition. This is a good place
    to play around with different collection types (list, tuple, set...),

    :param vec_1: a subscriptable collection of length 3
    :param vec_2: a subscriptable collection of length 3
    :return vec_3: a subscriptable collection of length 3
    """

    # add two vectors

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

    return vec_3

def normalize(vec):
    """
    From a length-3 vector return a normalized vector

    :param vec: a subscriptable collection of length 3
    :return norm_vec: a subscriptable collection 
    """

    # Calculate the length of the vector
    vec_len = 
    # Divide the components of vec by the length of the vector
    norm_vec = [_ / vec_len, _ / vec_len, _ / vec_len] 
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
    dot_product = vec_1[_] * vec_2[_] + vec_1[_] * vec_2[_] + vec_1[_] * vec_2[_]

    retrun dot_product

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
    cross_product_1 = vec_1[_] * vec_2[_] - vec_1[_] * vec_2[_]
    cross_product_2 = vec_1[_] * vec_2[_] - vec_1[_] * vec_2[_]
    cross_product_3 = vec_1[_] * vec_2[_] - vec_1[_] * vec_2[_]

    cross_product = [cross_product_1, cross_product_2, cross_product_3]

    return cross_product

 

