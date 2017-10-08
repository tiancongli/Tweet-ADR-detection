#coding=utf-8
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

DATASET = 'test'
#DATASET = 'dev'
#DATASET = 'train'

# define the source file, contains multiple feature columns, seperated by tab
SOURCE_FILE = '%s/%s_lss.txt' % (DATASET, DATASET)

# load the original features
original_features = []
with open(SOURCE_FILE) as f:
    for line in f:
        line = line.strip()
        original_features.append(line.split())

# create the polynomial features
feature_array = np.array(original_features, dtype=float)
poly = PolynomialFeatures(3)
output_array = poly.fit_transform(feature_array)

# output the new features
for row in output_array:
    print ','.join([str(item) for item in row[1:]])



