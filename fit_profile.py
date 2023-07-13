import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def plot_im(im, title="Image"):
    x_size = 389/60
    y_size = 292/60
    fig, ax = plt.subplots(figsize = (y_size, x_size))
    ax.axis("off")
    plt.pcolormesh(im, cmap = "Greys")
    plt.title(title)
    plt.show()
    
def plot_xslice(im, i_slice): # 2D plot of a slice
    in1D = im[i_slice, :]
    a = range(in1D.shape[0])
    #print(in1D.shape)
    fig, ax = plt.subplots()
    plt.plot(a, in1D)
    ax.set_xlabel("x (pixel)")
    ax.set_ylabel("Intensity (A.U.)")
    plt.show()

def plot_yslice(im, i_slice): # 2D plot of a slice
    in1D = im[:, i_slice]
    a = range(in1D.shape[0])
    #print(in1D.shape)
    fig, ax = plt.subplots()
    plt.plot(a, in1D)
    ax.set_xlabel("y (pixel)")
    ax.set_ylabel("Intensity (A.U.)")
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

# Find the dead pixels from blank image  
blank = read("BlankSample.png")
#plot_im(blank, "Empty")
#print(blank)
i_rm = np.array(np.where(blank>3)) # pixels which should be excluded

ex = read("ExampleImage.png")
#plot_im(ex, "Before cleaning")

cex = clean(ex, i_rm)
plot_im(cex, "After cleaning")

xc, yc = est_center(cex) #estimated centers

plot_xslice(cex, xc)
plot_yslice(cex, yc)


