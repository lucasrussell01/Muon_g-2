import ROOT as R
import numpy as np
import matplotlib.pyplot as plt
import glob as glob
from matcher import matcher



path = "../ToRFQstudy/run/data/" + "musr_11000.root"

m = matcher(path)

mis = m.fit()



