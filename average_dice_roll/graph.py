import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("rolls.csv")
num_simulations = int((data.shape[1] - 1) / 2)
print(num_simulations)
for i in range(num_simulations):
    mean_col_name = "mean" +  str(i)
    plt.plot(data["roll"], data[mean_col_name])
plt.xlabel("Number of Rolls")
plt.ylabel("Mean Dice Value")
plt.title("Dice Roll Simulator")
plt.xlim(left=1)
plt.ylim(3, 4)

plt.show()