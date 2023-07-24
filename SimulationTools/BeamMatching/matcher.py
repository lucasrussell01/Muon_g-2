import ROOT as R
import numpy as np
import matplotlib.pyplot as plt


class matcher:

    def __init__(self, file_path):
        
        self.f = R.TFile.Open(file_path, "read")
        self.tree = self.f.t1 
        self.n = self.tree.GetEntries()
        print("Processed file", self.f, "with entries:", int(self.n))

        self.alpha = 1.0745
        self.beta = 0.06740*100               *10
        self.epsilon = 0.167*5.0*1e-4/0.01    *10
        self.gamma = (1+self.alpha**2)/self.beta

    def fit(self):

        self.x = []
        self.xp = []
        self.y = []
        self.yp = []

        for i in range(self.n):
            self.tree.GetEntry(i)
            self.x.append(self.tree.save_x[0]-780.0)
            self.y.append(self.tree.save_y[0])        
            self.xp.append(self.tree.save_px[0]/self.tree.save_pz[0])
            self.yp.append(self.tree.save_py[0]/self.tree.save_pz[0])

        self.x = np.array(self.x)
        self.xp = np.array(self.xp)
        self.y = np.array(self.y)
        self.yp = np.array(self.yp)

        est_x_em = np.sqrt(np.mean(self.x*self.x)*np.mean(self.xp*self.xp) 
                    - np.mean(self.x*self.xp)**2)
        est_y_em = np.sqrt(np.mean(self.y*self.y)*np.mean(self.yp*self.yp) 
                    - np.mean(self.y*self.yp)**2)

        est_x_beta = np.std(self.x)**2/est_x_em
        est_x_gamma = np.std(self.xp)**2/est_x_em
        est_x_alpha = np.sqrt(est_x_beta*est_x_gamma-1)

        est_y_beta = np.std(self.y)**2/est_y_em
        est_y_gamma = np.std(self.yp)**2/est_y_em
        est_y_alpha = np.sqrt(est_y_beta*est_y_gamma-1)

        R_x = est_x_beta*self.gamma + est_x_gamma*self.beta - 2*self.alpha*est_x_alpha
        self.mis_x = np.sqrt(0.5*(R_x+np.sqrt(R_x**2-4)))-1

        R_y = est_y_beta*self.gamma + est_y_gamma*self.beta - 2*self.alpha*est_y_alpha
        self.mis_y = np.sqrt(0.5*(R_y+np.sqrt(R_y**2-4)))-1

        self.mis = np.sqrt(self.mis_x**2 +  self.mis_y**2)
        print("TOTAL MISMATCH: ", self.mis, "(x mismatch ", self.mis_x, ", y mismatch ", self.mis_y, ")")

        return self.mis

