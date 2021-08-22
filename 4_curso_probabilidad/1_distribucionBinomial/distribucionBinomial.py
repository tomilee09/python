import numpy as np
import matplotlib.pyplot as plt
from math import factorial
from numpy.random import binomial
from scipy.stats import binom

# crear la formula de la distribucion binomial (bernoulli)

def distBinomial(exitos, lanzamientos, probabilidadExito):
    return factorial(lanzamientos)/(factorial(exitos)*factorial(lanzamientos-exitos)) * pow(probabilidadExito, exitos) * pow(1-probabilidadExito, lanzamientos-exitos)
print(distBinomial(2, 3, 0.5)==3/8)

distribucion = binom(3, 0.5)
print(distribucion.pmf(2)==distBinomial(2, 3, 0.5))