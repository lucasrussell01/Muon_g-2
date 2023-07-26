import ROOT as R
import numpy as np
import matplotlib.pyplot as plt
import glob as glob
from matcher import matcher

base_path = "../../../ToRFQstudy/run/data/musr_" 


def plot(mismatch, x, x_title):
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot(x, mismatch, marker="o", markersize=4, linestyle="")
    ax.set_xlabel(x_title)
    ax.set_ylabel("Mismatch")
    ax.set_ylim(0, 2)
    ax.set_xlim(np.min(x)-0.3*np.min(x), np.max(x)+0.3*np.min(x))
    plt.show()

def vary_z_pos():
    n_runID = 11000 #start at 11000 then increment
    x = np.arange(1e-3, 10.5e-3, 0.5e-3)
    matches = []
    for z in x:
        path  = base_path + str(n_runID) + ".root"
        print("***** z position is ", z, "*****")
        try:
            m = matcher(path)
            mis = m.fit()
            matches.append(mis)
        except:
            matches.append(100)
            print("--------------------------------------------")
            print("   ")
            continue
        print("--------------------------------------------")
        print("   ")
        n_runID+=1
    return x, matches

def vary_y_pos():
    n_runID = 12000 
    x = np.arange(-23e-3, 24e-3, 1e-3)
    matches = []
    for y in x:
        path  = base_path + str(n_runID) + ".root"
        print("***** y position is ", y, "*****")
        try:
            m = matcher(path)
            mis = m.fit()
            matches.append(mis)
        except:
            matches.append(100)
            print("--------------------------------------------")
            print("   ")
            continue
        print("--------------------------------------------")
        print("   ")
        n_runID+=1
    return x, matches

def vary_z_size():
    n_runID = 13000 #start at 13000 then increment
    matches = []
    x =  np.arange(0, 7.5e-3, 0.25e-3)
    for z in x:
        path  = base_path + str(n_runID) + ".root"
        print("***** z beam size is ", z, "*****")
        try:
            m = matcher(path)
            mis = m.fit()
            matches.append(mis)
        except:
            matches.append(100)
            print("--------------------------------------------")
            print("   ")
            continue
        print("--------------------------------------------")
        print("   ")
        n_runID+=1
    return x, matches

def vary_y_size():
    n_runID = 14000 #start at 14000 then increment
    matches = []
    x =  np.arange(18e-3, 28.5e-3, 0.5e-3)
    for y in x:
        path  = base_path + str(n_runID) + ".root"
        print("***** y beam size is ", y, "*****")
        try:
            m = matcher(path)
            mis = m.fit()
            matches.append(mis)
        except:
            matches.append(100)
            print("--------------------------------------------")
            print("   ")
            continue
        print("--------------------------------------------")
        print("   ")
        n_runID+=1
    return x, matches


zpos, matches = vary_z_pos()
plot(matches, zpos, "Z position") 

ypos, matches = vary_y_pos()
plot(matches, ypos, "Y position") 

zbeam, matches = vary_z_size()
plot(matches, zbeam, "Z beam size") 

ybeam, matches = vary_y_size()
plot(matches, ybeam, "Y beam size") 



