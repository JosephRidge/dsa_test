# Check fro null values 
# Check percentage of null values per column
# Dropping all the columns with over 50% null values
# Imputing the remaining null values with mean

from eda_data import readData
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def checkNullValues(filePath):
    trainingDF = readData(filePath) 
    trainingDF.isnull().sum() 
    # return description

def checkDuplicates(filePath):
    trainingDF = readData(filePath)
    #Checking for duplicate values
    print(trainingDF.duplicated().sum())
    print("There are no duplicate values")

def replacingNullValuesWithMean(filePath):
    trainingDF = readData(filePath) 
    for i in trainingDF.columns[trainingDF.isnull().any(axis=0)]:
        trainingDF[i].fillna(trainingDF[i].mean(),inplace=True)
    # returm     

def checkForOutliers(filePath):
    # Checking for Outliers 
    trainingDF = readData(filePath) 
    col_names= trainingDF.drop(columns=['galaxy','ID']).columns.to_list()
    fig, ax = plt.subplots(len(col_names), figsize=(8,40))

    for i, col_val in enumerate(col_names):
        sns.boxplot(y=trainingDF[col_val],ax=ax[i])
        ax[i].set_title('Boxplot - {}'.format(col_val),fontsize=10)
        ax[i].set_xlabel(col_val, fontsize=8)
        plt.show()