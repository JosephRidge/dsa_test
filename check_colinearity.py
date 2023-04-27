

from eda_data import readData
import seaborn as sns
import matplotlib.pyplot as plt

def corelationCheck(filePath):
    trainingDF = readData(filePath)
    plt.figure(figsize=(12,10))
    cor = trainingDF.corr()
    sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
    plt.show()