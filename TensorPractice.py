import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib as plt
from tensorflow.keras.utils import plot_model

data = pd.read_csv('C:\Users\chera\OneDrive\Documents\SPRING 2022\ENGR 3398\MNIST.csv', sep=',')
data.head()