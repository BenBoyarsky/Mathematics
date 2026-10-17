import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("rolls.csv")

plt.plot(data["roll"], data["mean"])
plt.xlabel("Number of Rolls")
plt.ylabel("Mean Dice Value")
plt.title("Dice Roll Simulator")
plt.xlim(left=1)
plt.ylim(2, 4)

plt.show()