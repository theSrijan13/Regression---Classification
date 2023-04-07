#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


# In[4]:


X, y = make_blobs(n_samples=1000, centers=3, random_state=42)

# Initialize the KMeans object with the number of clusters to form and iterations
kmeans = KMeans(n_clusters=3, max_iter=300)

# Fit the data to the KMeans object
kmeans.fit(X)

# Get the cluster labels for each data point
labels = kmeans.labels_

# Use one-hot encoding to convert the labels into binary vectors
y = np.eye(3)[labels]
split_index = int(0.8 * len(X))
X_train, y_train = X[:split_index], y[:split_index]
X_test, y_test = X[split_index:], y[split_index:]

# Define the ANN model using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compile the model with a categorical cross-entropy loss and the Adam optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on the training set
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model on the testing set
accuracy = model.evaluate(X_test, y_test)[1]

print("Accuracy:", accuracy)

# Visualize the clustering and classification results
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].scatter(X[:, 0], X[:, 1], c=y.argmax(axis=1))
axs[0].set_title("True Labels")

# Plot the data points colored by their predicted labels
predicted_labels = model.predict(X).argmax(axis=1)
axs[1].scatter(X[:, 0], X[:, 1], c=predicted_labels)
axs[1].set_title("Predicted Labels")

plt.show()


# In[ ]:




