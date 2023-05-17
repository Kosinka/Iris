import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("iris.data")
print(type(dataset))
print(dataset.info())
print(dataset.columns)
print()
