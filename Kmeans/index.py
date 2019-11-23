import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import utils

x = np.random.rand(2, 1000) * 10

original_data = np.asarray(x).T

kmeans = KMeans(n_clusters=2, random_state=0).fit(original_data)
print(kmeans.cluster_centers_)
pred_label = kmeans.predict(original_data)
utils.kmeans_display(original_data, pred_label)