#lib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import seaborn as sns
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from scipy.spatial.distance import cdist, pdist
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN

#pio.renderers.default = 'png'
colors = ['#DB1C18', '#DBDB3B', '#51A2DB']
sns.set(palette=colors, font='Serif', style='white', rc={'axes.facecolor':'whitesmoke', 'figure.facecolor':'whitesmoke'})

def showpng(fig, name):
    fig.write_image(name)
    img = mpimg.imread(name)
    plt.imshow(img); plt.axis('off'); plt.show()

def overview(data, data_dict):
    #print(data.info()) #detail of column's value
    #print(data.shape) #column and row
    #print(data.describe()) #detail of data
    print(data.isnull().sum()) #check non-value or data.isna().sum()

def vis_n_proc(data, data_dict):
    fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10,6), constrained_layout=True)
    plt.suptitle('Univariated Data Analyis')
    ax = ax.flatten()
    int_cols = data.select_dtypes(exclude='object').columns
    for i, x in enumerate(int_cols):
        sns.histplot(data[x], ax=ax[i], kde=True, color=colors[2])
        #sns.boxplot(x=data[x], ax=ax[i], color=colors[0])
    plt.show()

def bivar_data_als(data, data_dict):
    """
    fig = px.scatter(data_frame=data, x='exports', y='imports', size='gdpp', text='country', color='gdpp', title='Country by Export & Import and corresponding GDP')
    showpng(fig, 'scatter_plot.png')
    """
    """
    int_cols = data.select_dtypes(exclude='object').columns
    for i in int_cols:
        fig = px.choropleth(data_frame=data, locationmode='country names', locations='country', color=i, title=f'{i} rate by countries')
        showpng(fig, 'choroleth_plot.png')
    """
    #sns.pairplot(data, corner=True)
    fig = plt.figure(figsize=(15,8))
    sns.heatmap(data.drop(columns='country').corr(), annot=True, square=True)
    plt.show()

def proc(data, data_dict):
    #print(data_dict)
    #print(data_dict)
    #overview(data, data_dict)
    #vis_n_proc(data, data_dict)
    bivar_data_als(data, data_dict)
