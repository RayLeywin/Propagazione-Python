import sympy as sp
import numpy as np
def propstat(f, x_val, y_val, z_val, w_val,u_val, sigma1):
    dati=np.array([x_val, y_val, z_val, w_val,u_val])
    #Definizione delle variabili
    x, y, z, w, u = sp.symbols('x y z w u')
    #Definizione della funzione
    #Calcolo del gradiente rispetto alle variabili x, y, z
    grad = sp.Matrix([sp.diff(f, var) for var in (x, y, z, w, u)])
    #Valutazione del gradiente in un punto specifico
    #Assegnazione dei valori alle variabili
    #Sostituzione dei valori nelle variabili
    grad_val = grad.subs({x: x_val, y: y_val, z: z_val, w: w_val, u:u_val})
    lunghezza=len(grad_val)
    somma=0
    for i in range(lunghezza):
        grad_val[i] = grad_val[i]**2 * sigma1[i]**2
        somma = grad_val[i]+ somma
    somma=somma**0.5
    return(somma)
def propmax(f, x_val, y_val, z_val, w_val,u_val, sigma1):
    #Definizione delle variabili
    x, y, z, w, u = sp.symbols('x y z w u')
    #Definizione della funzione
    #Calcolo del gradiente rispetto alle variabili x, y, z
    grad = sp.Matrix([sp.diff(f, var) for var in (x, y, z, w, u)])
    derivata=grad
    #Valutazione del gradiente in un punto specifico
    #Assegnazione dei valori alle variabili
    #Sostituzione dei valori nelle variabili
    grad_val = grad.subs({x: x_val, y: y_val, z: z_val, w: w_val, u:u_val})
    i=0
    lunghezza=len(grad_val)
    somma=0
    for i in range(lunghezza):
        grad_val[i] = abs(grad_val[i]) * sigma1[i]
        somma = (grad_val[i])+ somma
    return(somma)