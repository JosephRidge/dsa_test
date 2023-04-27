# read and explore the data set collected  :
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def readData(filePath):
    trainingDF = pd.read_csv(filePath)  
    return trainingDF

# get detailed summary of the dataframe ]
def getShape(filePath):
    trainingDF = readData(filePath)
    shape = trainingDF.shape()
    # print(f'SHAPE : {shape}')
    return shape


def getShape(filePath):
    trainingDF = readData(filePath)
    row,column = trainingDF.shape
    print(f'COLUMNS: {column} ROWS: {row}')


def getColumns(filePath):
    trainingDF = readData(filePath)
    columns = trainingDF.columns
    print(f'{columns}' )
    return columns


def getDescription(filePath):
    trainingDF = readData(filePath)
    description = trainingDF.describe()
    print(f'{description}')
    return description


def checkDuplicates(filePath):
    trainingDF = readData(filePath)
    # duplicate = trainingDF.duplicated.sum()
    print(f'{duplicate}')
    return duplicate


def checkMissingValues(filePath):
    trainingDF = readData(filePath)
    print(f'{trainingDF.ina().sum().sum()}')


#  returns the number of unique values for our target column
def getUniqueColumns(filePath, targetColumn, columnName):
    trainingDF = readData(filePath)
    print(f'{columnName}:', trainingDF[targetColumn].nunique())
    return 


# Preview Data Set
def previewData(filePath):
    trainingDF = readData(filePath)
    # trainingDF. 
    return 

 