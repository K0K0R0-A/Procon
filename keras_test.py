from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils
from sklearn.datasets import fetch_mldata
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

mnist = fetch_mldata('MNIST original')

x,y = mnist['data'],mnist['target']
x.shape
y.shape