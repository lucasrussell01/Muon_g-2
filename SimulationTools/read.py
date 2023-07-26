import ROOT as R
import numpy as np

path = "~/ToRFQstudy/run/data/musr_14015.root"

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

#for i in b:
 #   if "save" in i.GetName():
  #      print(i.GetName())

n = tree.GetEntries()
print("Number of entries in tree: ", int(n))

xnbin = 60
xmin  = -12
xmax  = 12
ynbin = 60
ymin  = -0.12
ymax  = 0.12
detector_cut = "save_detID==654&&save_particleID==-13"


hist = R.TH2F("hist","",xnbin, xmin, xmax, ynbin, ymin, ymax)
 

tree.Draw("save_px/save_pz:save_x-780 >> hist",detector_cut,"colz")


hist.SetXTitle("x")
hist.SetYTitle("x'  (px/pz)")
hist.SetTitle("Phase Space Histogram")
hist.Draw("colz")


raw_input("Press enter to close...")


hist = R.TH2F("hist","",xnbin, xmin, xmax, ynbin, ymin, ymax)
 

#tree.Draw("save_px/save_pz:save_x-780 >> hist",detector_cut,"colz")
tree.Draw("save_py/save_pz:save_y >> hist",detector_cut,"colz")


hist.SetXTitle("y")
hist.SetYTitle("y'  (px/pz)")
hist.SetTitle("Phase Space Histogram")
hist.Draw("colz")
raw_input("Press enter to close...")

f.Close()
