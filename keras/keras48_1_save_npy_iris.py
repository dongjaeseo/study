from sklearn.datasets import load_iris
import numpy as np

dataset = load_iris()
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
# print(dataset.keys())
x_data = dataset['data']
y_data = dataset.target
print(dataset.target_names)
print(dataset["DESCR"])
print(dataset["feature_names"])
print(dataset.filename)

print(type(x_data),type(y_data))

np.save('../data/npy/iris_x.npy', arr = x_data)
np.save('../data/npy/iris_y.npy', arr = y_data)