import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import yaml



class BeamFitter:


    def __init__(self, config):

        self.config = config
        self.path = config["Setup"]["path"]
        self.blank_path = self.path + "/" + config["Setup"]["blank"]
        self.distances = config["Setup"]["distances"]
                
        self.image_paths = [self.path + "/" + i for i in config["Setup"]["samples"]]

        self.show_beam = config["Setup"]["show_beam"]
        self.show_fit = config["Setup"]["show_fit"]

        self.blank_im = self.read(self.blank_path)
        self.i_rm = np.array(np.where(self.blank_im>3)) # indices to remove from all images

        self.x_width = []
        self.y_width = []

    def read(self, path): # read rgb image and convert to grayscale

        im = cv2.imread(path)
        gy = np.dot(im[...,:3], [0.3, 0.6, 0.1]).T# transpose to get correct orientation
        return gy

    def clean(self, im): # input grayscale image + 2D array of dead pixels

        for i in range(len(self.i_rm[0])):
            im[self.i_rm[0][i], self.i_rm[1][i]]=3 # set dead pixels to default 0 value
        im+=-3 # remove constant offset
        return im

    def plot_im(self, im, title="Image", center=True):

        x_size = 389/60
        y_size = 292/60
        fig, ax = plt.subplots(figsize = (y_size, x_size))
        plt.pcolormesh(im, cmap = "Greys", label = "Intensity (A. U.)")
        if center == True:
            xc, yc = self.est_center(im) 
            plt.plot(yc, xc, color = "red", markersize = 4, marker="o",linestyle="", label = "Estimated Center")
        plt.title(title) 
        plt.legend()
        ax.set_xlabel("x (pixel)")
        ax.set_ylabel("y (pixel)")
        plt.show()
    
    def pixel2um(self, val): # convert number of pixels to value in micrometers

        return val*1000/44 # 44 pixels is equivalent to 1000 um

    def est_center(self, im): # find beam center by simple mean

        ymean = np.mean(im, axis = 0)
        ymax = np.argmax(ymean)
        xmean = np.mean(im, axis = 1)
        xmax = np.argmax(xmean)
        print(f"Estimated position of beam centre is: {xmax, ymax}")
        return xmax, ymax

    def fit1D(self, im, axis, display=False): # 1D plot of a slice x direction
        
        xc, yc = self.est_center(im)
        if axis=="x":
            in1D = im[xc, :]
            c = xc
        elif axis=="y":
            in1D = im[:, yc]
            c = yc
        else:
            raise RuntimeError("Please choose x or y axis")
        
        def Gaussian1D(x, amplitude, x0, sigma_x):
            x0 = float(x0)   
            a = 1/(2*sigma_x**2)
            g = amplitude*np.exp(-(a*((x-x0)**2)))
            return g

        a = np.arange(in1D.shape[0])
        guess = (np.max(in1D), a[np.argmax(in1D)], c) 
        popt, pcov = opt.curve_fit(Gaussian1D, a, in1D, p0=guess, bounds=(0, np.inf))
        sig = round(self.pixel2um(popt[2]), 1)
        if display==True:
            fig, ax = plt.subplots()
            plt.plot(a, Gaussian1D(a, *popt), label = f"Fit: Sigma={sig} um")
            plt.plot(a, in1D, color = "black", marker="o", linestyle="", markersize=6, label="Data")
            ax.set_xlabel(f"{axis} (pixel)")
            ax.set_ylabel("Intensity (A.U.)")
            ax.text(0.01, 1.02, f"Beam Width ({axis}): {4*sig} um", fontsize=12, weight="bold", transform=ax.transAxes)
            plt.legend()
            plt.show()
        print(f"Fitted beam width in {axis} direction is: {4*sig}um")
        return 4*sig

    def fit_all(self):

        for i in range(len(self.image_paths)):
            im = self.clean(self.read(self.image_paths[i]))
            if self.show_beam==True:
                self.plot_im(im, f"{str(self.distances[i])} cm", center=True)
            if self.show_fit==True:
                self.x_width.append(self.fit1D(im, 'x', display = True))
                self.y_width.append(self.fit1D(im, 'y', display = True))
            else:
                self.x_width.append(self.fit1D(im, 'x'))
                self.y_width.append(self.fit1D(im, 'y'))

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,6))
        ax1.scatter(self.distances, self.x_width, color = "Black")
        ax1.set_xlabel("Distance (cm)")
        ax1.set_ylabel("Beam width (um)")
        ax1.text(0.05, 0.9, r"X Beam Width", fontsize=12, weight="bold", transform=ax1.transAxes)
        ax2.scatter(self.distances, self.y_width, color = "Black")
        ax2.set_xlabel("Distance (cm)")
        ax2.set_ylabel("Beam width (um)")
        ax2.text(0.05, 0.9, r"Y Beam Width", fontsize=12, weight="bold", transform=ax2.transAxes)
        plt.show()





config = yaml.safe_load(open("config.yaml"))

fitter = BeamFitter(config)
fitter.fit_all()


