from eda_data import readData,getShape, getColumns, getDescription,getUniqueColumns, checkMissingValues
from clean_data import checkForOutliers,checkNullValues, checkDuplicates,replacingNullValuesWithMean
from check_colinearity import corelationCheck
"""
# Perfoming Explorative Data Anaylysis 
    Defining the question
    Defining the metric of success
    Importing Libraries
    Loading the dataset
    Previewing the dataset
    Cleaning the dataset
    Checking multicolineality
    Encoding the object variable
    Univariate analysis
    spliting the dataset
    Implementing Lasso regression
"""

def perfomEDA(filePath, targetData): 
    print(f"============  TARGET DATA-SET USED: {targetData}  ============")
    print('START of SUMMARY') 
    print('* DECRIPTION *')
    getDescription(filePath)
    print('* SIZE *')
    getShape(filePath)
    print('* UNIQUE GALAXIES & YEARS *')
    getUniqueColumns(filePath,'galactic year','Number of galactic years')
    getUniqueColumns(filePath,'galaxy','number of galaxies')
    print('END of SUMMARY')

def cleanData(filePath):
    print(f"============  CLEANING DATA  ============")
    print('START of CLEANING ..... ') 
    print('check null values ')
    checkNullValues(filePath)
    print('remove null values')
    replacingNullValuesWithMean(filePath)
    print('start of check duplicates...')
    checkDuplicates(filePath)
    print('...end of check duplicates')
    print('start of check for outliers...')
    # checkForOutliers(filePath) #todo: return once done
    print('...end of check outliers')
    print(f"============  END OF CLEANING DATA  ============")

def checkColinearlity(filePath):
    print(f"============  COLINEARITY CHECK   ============")
    corelationCheck(filePath)


if __name__ == '__main__':
    print("starting... ")
    # perfom Explorative Data Analyiss

    # EDA ON TRAINED DATA
    perfomEDA('data/Train_data.csv', '*TRAINING DATA*')
    # EDA ON VALIDATED DATA
    perfomEDA('data/Validation.csv', '*VALIDATION DATA*')

    # cleaning 
    cleanData('data/Train_data.csv')  
    cleanData('data/Validation.csv')  
    # corelations
    checkColinearlity('data/Validation.csv')

