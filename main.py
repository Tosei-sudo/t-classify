# coding: utf-8

import os
from matplotlib import pyplot as plt
import numpy as np
from scipy.spatial import cKDTree
import time
import copy

from data import get_random_data
from model import SetModel

start = time.time()

model_data = get_random_data(300)
data = np.array([
    [d.meta_1, d.meta_2] for d in model_data
], dtype=np.float32)
print(data.shape)

# ここまでデータ生成

model_dict = {model.id: model for model in model_data}

n = 3

max_y = data[:, 1].max()
min_y = data[:, 1].min()

x_diff = 360 / n
y_diff = (max_y - min_y) / n

# Extend the data to create a grid-like structure
extend_id_data = [model.id for model in model_data]
indexies = np.where(data[:, 0] < (x_diff * (n - 1)))
for index in indexies[0]:
    extend_id_data.append(model_data[index].id)

extend_data = np.append(data, data[(data[:, 0] < (x_diff * (n - 1))), :] + np.array([[360, 0]]), axis=0)

normalized_data = np.array([
    extend_data[:, 0] / 360,
    (extend_data[:, 1] - min_y) / (max_y - min_y)
]).T

data_tree = cKDTree(normalized_data)

pairing_index = []

for i in range(n):
    ideal_coordinates = data + np.array([[x_diff * i, y_diff * i]])
    mask = (ideal_coordinates[:, 1] > max_y)
    ideal_coordinates[mask, 1] = min_y + (ideal_coordinates[mask, 1] - max_y)

    normalized_ideal_coordinates = np.array([
        ideal_coordinates[:, 0] / 360,
        (ideal_coordinates[:, 1] - min_y) / (max_y - min_y)
    ]).T
    
    d, index = data_tree.query(normalized_ideal_coordinates)

    pairing_index.append(index)

pairing_index = np.array(pairing_index).transpose(1, 0)

score_models = [SetModel(0, [model_dict.get(extend_id_data[i]) for i in row]) for row in pairing_index]

print(score_models)

print(time.time() - start)

plt.scatter(extend_data[:, 0], extend_data[:, 1], alpha=0.5)
for pairing in pairing_index:
    plt.plot(extend_data[pairing, 0], extend_data[pairing, 1], alpha=0.5)

plt.title('Random Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()