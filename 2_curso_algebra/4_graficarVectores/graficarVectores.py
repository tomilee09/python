import matplotlib.pyplot as plt
import numpy as np

def graficarVectores(vectores, alpha = 1):

    plt.figure()
    plt.axvline(x=0, color = 'grey', zorder =0)
    plt.axhline(y=0, color = 'grey', zorder =0)

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for i in range(len(vectores)):
        min_x = min(vectores[i][0],min_x) 
        max_x = max(vectores[i][0],max_x)  
        min_y = min(vectores[i][1],min_y)
        max_y = max(vectores[i][1],max_y)  
    plt.xlim(min_x-1,max_x+1)
    plt.ylim(min_y-1,max_y+1)

    for i in range(len(vectores)):
        x = np.concatenate([[0,0], vectores[i]])
        plt.quiver(
            x[0],
            x[1],
            x[2],
            x[3],
            angles='xy', scale_units='xy', scale=1, alpha=alpha
        )
