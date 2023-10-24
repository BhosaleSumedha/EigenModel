# -*- coding: utf-8 -*-
"""Eigenvalues_Eigenvectors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qtbhk1UapKoInNiwcbx3CtwlY80k81p9
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

import sys
# Change the path as per your system
sys.path.append("/home/sumedha/Documents/Subjects/Mathematics/Project")
df = pd.read_csv("Breast_Cancer.csv")

categorical_features = df.select_dtypes(include = "object").columns
numerical_features = df.select_dtypes(include = "int64").columns

from sklearn.preprocessing import LabelEncoder

# Apllying LabelEncoder to all categorical features
df[categorical_features] = df[categorical_features].apply(LabelEncoder().fit_transform)

# Displaying first 5 rows
#df.head()

from sklearn.preprocessing import RobustScaler, StandardScaler

# Saving tumor size for later
tumor_sizes = df["Tumor Size"].to_numpy()

# Applying RobustScaler to scale orginal numerical features
df[numerical_features] = RobustScaler().fit_transform(df[numerical_features])

# Displaying first 5 rows
df.describe()

corr_matrix = np.round(np.corrcoef(df.T),2)
# Plotting the correlation matrix
plt.figure(figsize=(14,11))
sns.heatmap(corr_matrix, cmap='viridis', annot=True,
            xticklabels=('X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16'), yticklabels=('X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16')
           )
plt.title("Correlation Matrix");

# To cutoff
#threshold = 0.9

#def high_cor_function(df):
#    cor = df.corr()
#    corrm = np.corrcoef(df.T)
#    corr = corrm - np.diagflat(corrm.diagonal())
#    print("max corr:",corr.max(), ", min corr: ", corr.min())
#    c1 = cor.stack().sort_values(ascending=False).drop_duplicates()
#    high_cor = c1[c1.values!=1]
#    thresh = threshold
#    display(high_cor[high_cor>thresh])

#high_cor_function(df)

#Dropping highly correlated variables
#target='Tumor Size'
#X_drop = df.drop(columns=['Tumor Size', 'T Stage ', 'N Stage', '6th Stage', 'Reginol Node Positive'])

#y = df[target]

#X_drop

# Correlation after dropping highly correlated
#corr_matrix_xdrop = np.corrcoef(X_drop.T)
#eig_vals_xdrop, eig_vecs_xdrop = np.linalg.eig(corr_matrix_xdrop)


#eigenvectors_cor_xdrop=pd.DataFrame(eig_vecs_xdrop, columns=(eig_vals_xdrop))
#eigenvectors_cor_xdrop

# Using original dataframe getting eigenvalue decomposition
corr_matrix_original = np.corrcoef(df.T)
eig_vals_ori, eig_vecs_ori = np.linalg.eig(corr_matrix_original)


eigenvectors_ori=pd.DataFrame(eig_vecs_ori, columns=(eig_vals_ori))
eigenvectors_ori

# plotting eigenvalues in decreasing order

import numpy as np
import matplotlib.pyplot as plt

# Assuming you have a matrix 'eigenvalue_matrix' where each column represents an eigenvalue
sorted_eigenvalues = np.sort(eig_vals_ori)[::-1]
# Create a plot
plt.figure()
plt.plot(sorted_eigenvalues, marker='o', linestyle='-')
plt.xlabel('Eigenvalue Index')
plt.ylabel('Eigenvalue Magnitude')
plt.title('Eigenvalues Plot')

# Display the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt

#eig_vals_ori, eig_vecs_ori
# Sort eigenvalues in descending order
sorted_indices = np.argsort(eig_vals_ori)[::-1]
sorted_eigenvalues = eig_vals_ori[sorted_indices]
sorted_eigenvectors = eig_vecs_ori[:, sorted_indices]

# Create a plot for eigenvectors magnitude

all_eigenvector_names = ('X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16')

# Select the eigenvectors corresponding to the highest eigenvalue
highest_eigenvalue_idx = 0
eigenvectors_highest = sorted_eigenvectors[:, highest_eigenvalue_idx]

# Sort eigenvectors by magnitude in decreasing order
sorted_indices_highest = np.argsort(np.abs(eigenvectors_highest))[::-1]
sorted_eigenvectors_highest = eigenvectors_highest[sorted_indices_highest]

# Select the eigenvectors corresponding to the second highest eigenvalue
second_highest_eigenvalue_idx = 1
eigenvectors_second_highest = sorted_eigenvectors[:, second_highest_eigenvalue_idx]

# Sort eigenvectors by magnitude in decreasing order
sorted_indices_second_highest = np.argsort(np.abs(eigenvectors_second_highest))[::-1]
sorted_eigenvectors_second_highest = eigenvectors_second_highest[sorted_indices_second_highest]

# Select the names of the eigenvectors corresponding to the sorted indices
eigenvector_names_highest = [all_eigenvector_names[i] for i in sorted_indices_highest]
eigenvector_names_second_highest = [all_eigenvector_names[i] for i in sorted_indices_second_highest]

# Create a plot for eigenvectors magnitude
plt.figure()
plt.plot(np.abs(sorted_eigenvectors_highest), marker='o', label='Highest Eigenvalue Index')
plt.plot(np.abs(sorted_eigenvectors_second_highest), marker='o', label='Second Highest Eigenvalue Index')
plt.xlabel('Eigenvector')
plt.ylabel('Eigenvector Magnitude')
plt.title('Eigenvectors Magnitude')

# Set the x-axis tick labels as eigenvector names
plt.xticks(range(len(eigenvector_names_highest)), eigenvector_names_highest, rotation=90)

# Display the legend
plt.legend()

# Display the plot
plt.show()

# without abs magnitude
import numpy as np
import matplotlib.pyplot as plt

#eig_vals_ori, eig_vecs_ori
# Sort eigenvalues in descending order
sorted_indices = np.argsort(eig_vals_ori)[::-1]
sorted_eigenvalues = eig_vals_ori[sorted_indices]
sorted_eigenvectors = eig_vecs_ori[:, sorted_indices]

# Create a plot for eigenvectors magnitude

all_eigenvector_names = ('X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16')

# Select the eigenvectors corresponding to the highest eigenvalue
highest_eigenvalue_idx = 0
eigenvectors_highest = sorted_eigenvectors[:, highest_eigenvalue_idx]

# Sort eigenvectors by magnitude in decreasing order
sorted_indices_highest = np.argsort(eigenvectors_highest)[::-1]
sorted_eigenvectors_highest = eigenvectors_highest[sorted_indices_highest]

# Select the eigenvectors corresponding to the second highest eigenvalue
second_highest_eigenvalue_idx = 1
eigenvectors_second_highest = sorted_eigenvectors[:, second_highest_eigenvalue_idx]

# Sort eigenvectors by magnitude in decreasing order
sorted_indices_second_highest = np.argsort(eigenvectors_second_highest)[::-1]
sorted_eigenvectors_second_highest = eigenvectors_second_highest[sorted_indices_second_highest]

# Select the names of the eigenvectors corresponding to the sorted indices
eigenvector_names_highest = [all_eigenvector_names[i] for i in sorted_indices_highest]
eigenvector_names_second_highest = [all_eigenvector_names[i] for i in sorted_indices_second_highest]

# Create a plot for eigenvectors magnitude
plt.figure()
plt.plot(sorted_eigenvectors_highest, marker='o', label='Highest Eigenvalue Index')
plt.plot(sorted_eigenvectors_second_highest, marker='o', label='Second Highest Eigenvalue Index')
plt.xlabel('Eigenvector')
plt.ylabel('Eigenvector Magnitude')
plt.title('Eigenvectors Magnitude')

# Set the x-axis tick labels as eigenvector names
plt.xticks(range(len(eigenvector_names_highest)), eigenvector_names_highest, rotation=90)

# Display the legend
plt.legend()

# Display the plot
plt.show()

# code to plot eigenvectors without sorting
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have eigenvectors stored in a numpy array 'eigenvectors'
# eigenvectors.shape = (num_features, num_eigenvectors)

# Select the eigenvectors for the first and second highest eigenvalues
eigenvectors_1 = eig_vecs_ori[:, 0]
eigenvectors_2 = eig_vecs_ori[:, 1]

# Get the feature names for the x-axis
feature_names = ('X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12','X13','X14','X15','X16')
#feature_names = df.columns

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the eigenvectors
ax.plot(range(len(feature_names)), eigenvectors_1, marker='o', label='First Eigenvector')
ax.plot(range(len(feature_names)), eigenvectors_2, marker='o', label='Second Eigenvector')

# Set the x-axis tick labels as feature names
ax.set_xticks(range(len(feature_names)))
ax.set_xticklabels(feature_names, rotation=90)

# Set the y-axis label and title
ax.set_ylabel('Eigenvector Magnitude')
ax.set_title('Eigenvectors for First and Second Highest Eigenvalues')

# Add legend and grid
ax.legend()
ax.grid(False)

# Adjust the layout to prevent overlap of tick labels
fig.tight_layout()

# Show the plot
plt.show()



eigenvectors_first2=pd.DataFrame()
eigenvectors_first2['3.744']=sorted_eigenvectors_highest
eigenvectors_first2['1.699']=sorted_eigenvectors_second_highest
eigenvectors_first2

# Dropping first four eigenvectors corresponding to highly correlated variables
X=eigenvectors_first2.iloc[5:16,:]
X

Y=eigenvectors_first2.iloc[4,:]
Y

# with dropping variables - highly correlated
from sklearn.decomposition import PCA
pca_xdrop = PCA()
pca_xdrop = pca_xdrop.fit(X_drop)
plt.bar(np.arange(0,11), pca_xdrop.explained_variance_ratio_)
plt.xlabel("Component number")
plt.ylabel("Proportion of Variance")
plt.title("Scree Plot")

#########################################################################



