import graphlib
import numpy as np
import pandas as pd
import csv
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib.animation as FuncAnimation


data = pd.read_csv("C:/users/mstan/project/Data/Simulation_0/Occlusion_6/OcclusionCoordinates.csv")
X = data['X'].tolist()
Y = data['Y'].tolist()

Action = pd.read_csv("C:/Users/mstan/project/Data/Simulation_0/Occlusion_6/predator_1/Depth_5000/Episode_1.csv")
AgentX = Action['Agent X'].tolist()
AgentY = Action['Agent Y'].tolist()
PredatorX = Action['Predator X'].tolist()
PredatorY = Action['Predator Y'].tolist()

M = np.zeros((15,15))
for i in range(len(X)):
    M[14-Y[i]][X[i]] = -1
    
plt.imshow(M, cmap='gray')
plt.show()