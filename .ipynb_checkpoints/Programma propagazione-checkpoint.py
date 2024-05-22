import numpy as np
import math
from sympy import *
import pandas as pd
from propagazione import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
x,y,z,w,u = symbols('x y z w u')
f=x/y
x_val= 5893*10**-10
y_val= 0.3581
z_val= 0
w_val=0
u_val=0
sigmax= 3*10**-10
sigmay= 0.3162*3
sigmaz= 0
sigmaw=0
sigmau= 0
sigma1=np.array([sigmax,sigmay,sigmaz,sigmaw,sigmau])
s=propmax(f,x_val,y_val,z_val,w_val,u_val,sigma1)*10**10
print(s)