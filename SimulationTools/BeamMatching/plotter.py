import matplotlib.pyplot as plt
import numpy as np


def plot(mismatch, var, var_name, n, nion, x, y, xp, yp):

    fig, ax = plt.subplots(2, 3, figsize=(20, 10))

    ax[0][0].grid()
    ax[0][0].plot(var, mismatch, marker="o", markersize=4, linestyle="")
    ax[0][0].set_xlabel(var_name)
    ax[0][0].set_ylabel("Mismatch")
    #ax[0][0].set_ylim(0, 2)
    #ax[0][0].set_xlim(np.min(var)-0.3*np.min(var), np.max(var)+0.3*np.min(var))

    ax[0][1].grid()
    ax[0][1].plot(var, x, marker="o", markersize=4, linestyle="")
    ax[0][1].set_xlabel(var_name)
    ax[0][1].set_ylabel("Mean x")

 
 
    ax[0][2].grid()
    ax[0][2].plot(var, y, marker="o", markersize=4, linestyle="")
    ax[0][2].set_xlabel(var_name)
    ax[0][2].set_ylabel("Mean y")

  
    ax[1][0].grid() 
    ax[1][0].plot(var, n, marker="o", markersize=4, linestyle="", label  = "Number at Target")
    ax[1][0].plot(var, nion, marker="o", markersize=4, linestyle="", label  = "Number Ionised")
    ax[1][0].legend()
    ax[1][0].set_xlabel(var_name)
    ax[1][0].set_ylabel("Events")


    ax[1][1].grid()
    ax[1][1].plot(var, xp, marker="o", markersize=4, linestyle="")
    ax[1][1].set_xlabel(var_name)
    ax[1][1].set_ylabel("Mean x'")


    ax[1][2].grid()
    ax[1][2].plot(var, yp, marker="o", markersize=4, linestyle="")
    ax[1][2].set_xlabel(var_name)
    ax[1][2].set_ylabel("Mean y'")
   
    fig.subplots_adjust(wspace=0.3)

    plt.show()


