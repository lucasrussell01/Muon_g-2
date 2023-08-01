import ROOT as R
import numpy as np
import matplotlib.pyplot as plt
import glob as glob
from matcher import matcher
from plotter import plot

path = "../../../ToRFQstudy/run/data/" 

def vary_z_pos():
    n_runID = 31000 #start at 11000 then increment
    var = np.arange(1e-3, 10.5e-3, 0.25e-3)
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    for z in var:
        print("   ")
        print("--------------------------------------------")
        print("z position:", z)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(z)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp

def vary_y_pos():
    n_runID = 32000 
    var = np.arange(-23e-3, 24e-3, 1e-3)
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    for y in var:
        print("   ")
        print("--------------------------------------------")
        print("y position is ", y)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(y)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp

def vary_z_size():
    n_runID = 33000 #start at 13000 then incrementi
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    var =  np.arange(0, 7.5e-3, 0.1e-3)
    for z in var:
        print("   ")
        print("--------------------------------------------")
        print("z beam size is ", z)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(z)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp

def vary_y_size():
    n_runID = 34000 #start at 14000 then increment
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    var =  np.arange(18e-3, 28.5e-3, 0.5e-3)
    for y in var:
        print("   ")
        print("--------------------------------------------")
        print("y beam size is ", y)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(y)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp

def vary_VUV_E():
    n_runID = 15000 #start at 15000 then increment
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    var =  np.arange(80e-6, 122e-6, 2e-6)
    for e in var:
        print("   ")
        print("--------------------------------------------")
        print("VUV Energy ", e)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(e)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp

def vary_UNB_E():
    n_runID = 16000 #start at 16000 then increment
    valid = []
    matches = []
    n_hit = []
    n_ion = []
    mean_x = []
    mean_y = []
    mean_xp = []
    mean_yp = []
    var =  np.arange(0.24, 0.37, 0.01)
    for e in var:
        print("   ")
        print("--------------------------------------------")
        print("UNB Energy ", e)
        try:
            m = matcher(path, n_runID)
            mis, n, nion, xm, xpm, ym, ypm  = m.fit()
            valid.append(e)
            matches.append(mis)
            n_hit.append(n)
            n_ion.append(nion)
            mean_x.append(xm)
            mean_xp.append(xpm)
            mean_y.append(ym)
            mean_yp.append(ypm)
            n_runID+=1
        except:
            n_runID+=1
            continue
    return valid, matches, n_hit, n_ion, mean_x, mean_y, mean_xp, mean_yp




