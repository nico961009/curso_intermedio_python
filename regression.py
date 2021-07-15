import numpy as np #libreria que sirve para sumas y promedios. El "as" se utiliza para poder llamar a la libreria de una amnera más comoda.
import matplotlib.pyplot as plt #libreria que sirve para graficar.

def estimate_b0_b1(x,y):
    n = np.size(x) #size  define el tamaño de x.
    #obtenemos los promedios de "x" y de "y"
    m_x, m_y = np.mean(x), np.mean(y)

    #Calcular mi sumatoria de XY y mi sumatoria XX
    Sumatoria_xy= np.sum((x-m_x)*(y-m_y)) #sum es para sumar todo el array.
    Sumatoria_xx= np.sum((x-m_x)**2)

    #Coeficiente de regresión
    b_1 = Sumatoria_xy / Sumatoria_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

print (estimate_b0_b1([1,2,3,4,5],[1,3,4,6,8]))