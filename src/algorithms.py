#lib
import joblib
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def showpng(fig, name):
    fig.write_image(name)
    img = mpimg.imread(name)
    plt.imshow(img); plt.axis('off'); plt.show()

def pca(data, data_dict):
    data_scaled = StandardScaler().fit_transform(data.drop(['country'], axis=1))
    #print(data_scaled)
    decom = PCA(svd_solver='auto')
    decom.fit(data_scaled)
    cum_exp_ratio = np.cumsum(np.round(decom.explained_variance_ratio_, 2))
    #print(cum_exp_ratio)
    fig = plt.figure(figsize=(10,8))
    ax = sns.lineplot(y=cum_exp_ratio, x=np.arange(0, len(cum_exp_ratio)))
    ax = sns.scatterplot(y=cum_exp_ratio, x=np.arange(0, len(cum_exp_ratio)))
    ax.set_xlabel('No of components')
    ax.set_ylabel('Explaned variance ratio')
    #joblib.dump(decom, 'pca_model.pkl')

    plt.show()

def proc(data, data_dict):
    #print("Data\n", data)
    pca(data, data_dict)
