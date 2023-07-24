import ROOT as R
import numpy as np

path = "~/ToRFQstudy/run/data/musr_10000.root"

f = R.TFile.Open(path, "read")


def inspect(file):
    keys = file.GetListOfKeys()
    print("Inspecting file: ", file.GetName())
    for key in keys:
        print(key.GetName())
        print(key.GetClassName())
        print("**********")


inspect(f)

tree = f.t1 

b = tree.GetListOfBranches()

#print(b)
for i in b:
    if "save" in i.GetName():
        print(i.GetName())

n = tree.GetEntries()
print("Number of entries in tree: ", int(n))

#for i in range(n):
 #   tree.GetEntry(i)
  #  print(tree.fH_x)


xnbin = 60
xmin  = -12
xmax  = 12
ynbin = 60
ymin  = -0.12
ymax  = 0.12
detector_cut = 'save_detID==654&&save_particleID==-13'

alpha = 1.0745
beta = 0.06740*100               *10
epsilon = 0.167*5.0*1e-4/0.01    *10


hist = R.TH2F("hist","",xnbin, xmin, xmax, ynbin, ymin, ymax)
 

tree.Draw("save_px/save_pz:save_x-780 >> hist",detector_cut,"colz")

hist.SetXTitle("x")
hist.SetYTitle("x'  (px/pz)")
hist.SetTitle("Phase Space Histogram")
hist.Draw("colz")


#import time
#time.sleep(10)

raw_input("Press enter to close...")

f.Close()
