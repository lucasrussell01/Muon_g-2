import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def rgb2gray(rgb): # convert rgb to grayscale
    return np.dot(rgb[...,:3], [0.3, 0.6, 0.1])

def read(path): # read and convert to grayscale
    im = cv2.imread(path)
    gy = rgb2gray(im).T # transpose to get correct orientation
    return gy

def clean(im, dead_index): # input grayscale image + 2D array of dead pixels
    for i in range(len(dead_index[0])):
        im[dead_index[0][i], dead_index[1][i]]=8.4 # set dead pixels to default 0 value
    im+=-3 # remove constant offset
    return im

def plot_im(im, title="Image", center=False):
    x_size = 389/60
    y_size = 292/60
    fig, ax = plt.subplots(figsize = (y_size, x_size))
    plt.pcolormesh(im, cmap = "Greys", label = "Intensity (A. U.)")
    if center == True:
        xc, yc = est_center(im) 
        plt.plot(yc, xc, color = "red", markersize = 1, marker="o",linestyle="", label = "Estimated Center")
    plt.title(title) 
    plt.legend()
    ax.set_xlabel("x (pixel)")
    ax.set_ylabel("y (pixel)")
    plt.show()
    
def pixel2um(val): # convert number of pixels to value in micrometers
    return val*1000/44 # 44 pixels is equivalent to 1000 um

def est_center(im): # find beam center by simple mean
    ymean = np.mean(im, axis = 0)
    ymax = np.argmax(ymean)
    xmean = np.mean(im, axis = 1)
    xmax = np.argmax(xmean)
    print(f"Estimated position of beam centre is: {xmax, ymax}")
    return xmax, ymax

def Gaussian1D(x, amplitude, x0, sigma_x):
    x0 = float(x0)   
    a = 1/(2*sigma_x**2)
    g = amplitude*np.exp(-(a*((x-x0)**2)))
    return g

def fit1D(im, axis, verbose=False): # 1D plot of a slice x direction
    xc, yc = est_center(im)
    if axis=="x":
        in1D = im[xc, :]
        c = xc
    elif axis=="y":
        in1D = im[:, yc]
        c = yc
    else:
        raise RuntimeError("Please choose x or y axis")
    a = np.arange(in1D.shape[0])
    guess = (np.max(in1D), a[np.argmax(in1D)], c) 
    popt, pcov = opt.curve_fit(Gaussian1D, a, in1D, p0=guess)
    sig = round(pixel2um(popt[2]), 1)
    if verbose==True:
        fig, ax = plt.subplots()
        plt.plot(a, Gaussian1D(a, *popt), label = f"Fit: Sigma={sig} um")
        plt.plot(a, in1D, color = "black", marker="o", linestyle="", markersize=4, label="Data")
        ax.set_xlabel(f"{axis} (pixel)")
        ax.set_ylabel("Intensity (A.U.)")
        ax.text(0.01, 1.02, f"Beam Width ({axis}): {4*sig} um", fontsize=12, weight="bold", transform=ax.transAxes)
        plt.legend()
        plt.show()
    print(f"Fitted beam width in {axis} direction is: {4*sig}um")
    return sig


# Find the dead pixels from blank image  
blank = read("BlankSample.png")
i_rm = np.array(np.where(blank>3)) # pixels which should be excluded

im = read("ExampleImage.png")
im = clean(im, i_rm)

#plot_im(im, "After cleaning", center=True)

fit1D(im, 'x')#, verbose = True)
fit1D(im, 'y')#, verbose = True)

