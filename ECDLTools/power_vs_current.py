import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("diode_power.csv")
df2 = pd.read_csv("ECDL_power_tuned.csv")
df3 = pd.read_csv("ECDL_power_untuned.csv")



diode_current = df1["Current (mA)"]
diode_power = df1["Power (mW)"]

ECDL_tuned_current = df2["Current (mA)"]
ECDL_tuned_power = df2["Power (mW)"]

ECDL_untuned_current = df3["Current (mA)"]
ECDL_untuned_power = df3["Power (mW)"]

fig, ax = plt.subplots()
ax.set_axisbelow(True)
plt.grid()
plt.scatter(diode_current, diode_power, color = "black", label = "Laser Diode")
plt.scatter(ECDL_tuned_current, ECDL_tuned_power, color = "red", label = "Tuned ECDL")
plt.scatter(ECDL_untuned_current, ECDL_untuned_power, color = "blue", label = "Untuned ECDL")
ax.set_xlabel("Current (mA)")
ax.set_ylabel("Power (mW)")
plt.legend()
plt.show()
