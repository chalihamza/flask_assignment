from django.contrib.admin import display
from tensorflow import keras
# import tensorflow.keras as tk
import random
import collections
import numpy as np
import matplotlib.pyplot as plt


def display_random_images_with_labels(d, n=10):
    """
        accept dataset in tuple form, first index
        is np arrays (images) and second is labels
        and display n random images with labels
        from it
        Inputs:
            d (tuple): dataset images, dataset labels on same indexs
            n (int): number of samples to display (default: 10)
        Output:
            None
    """
    choices = list(range(len(d[0])))
    for i in range(n):
        index = random.choice(choices)
        choices.remove(index)
        print("index:", index)
        print("Lable:", d[1][index])
        plt.imshow(d[0][index], cmap='gray')
        plt.show()


# import dataset

dataset = keras.datasets.mnist.load_data()

print("There are", len(dataset[0][0]), "images in training dataset")

print("There are", len(dataset[1][0]), "images in training dataset")

print("___________________")

# end of emport dataset

# for checking shap of dataset
print(dataset[0][0][0].shape)

# prenting random image
print("Randomly printing 10 images with labels from training dataset")

display_random_images_with_labels(dataset[0])

print("There are", len(dataset[0][1]), "labels in training dataset for", len(dataset[0][0]),
      "images in training dataset")

print("There are", len(dataset[1][1]), "labels in training dataset for", len(dataset[1][0]),
      "images in training dataset")

print("There are", len(set(dataset[0][1])), "unique classes in training dataset")

print(
    "Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")

display(collections.Counter(dataset[0][1]))

print("There are", len(set(dataset[1][1])), "unique classes in validation dataset")

print(
    "Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")

display(collections.Counter(dataset[1][1]))

# code of reduce the size of picture

new_x = []
new_y = []

for labels in range(10):
    indices_training = np.where(dataset[0][1] == labels)[0]
    indices_training = indices_training[:600]
    new_x.append(dataset[0][0][indices_training])
    new_y.append(dataset[0][1][indices_training])
new_x = np.concatenate(new_x)
new_y = np.concatenate(new_y)

test_x = []
test_y = []
for labels in range(10):
    indices_test = np.where(dataset[1][1] == labels)[0]
    indices_test = indices_test[:100]
    test_x.append(dataset[0][0][indices_test])
    test_y.append(dataset[0][1][indices_test])
test_x = np.concatenate(test_x)
test_y = np.concatenate(test_y)

new_dataset = ((new_x, new_y), (test_x, test_y))

# prenting new data set

# Checking the shape of first image in new training dataset
print(new_dataset[0][0][0].shape)
print("___________________")

# Checking the size of dataset
print("There are", len(new_dataset[0][1]), "labels in training dataset for", len(new_dataset[0][0]),
      "images in training dataset")
print("There are", len(new_dataset[1][1]), "labels in validation dataset for", len(new_dataset[1][0]),
      "images in validation dataset")
print("___________________")

# Checking the number of images per class
print("There are", len(set(new_dataset[0][1])), "unique classes in training dataset")
print(
    "Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(new_dataset[0][1]))
print("There are", len(set(new_dataset[1][1])), "unique classes in validation dataset")
print(
    "Breakdown of each labels is below (format: dict key is label, dict value is occurrence of that label/ number of images for that label)")
display(collections.Counter(new_dataset[1][1]))
