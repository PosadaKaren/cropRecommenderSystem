from asyncio.windows_events import NULL
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import pearsonr
import statistics
import numpy as np
import pandas as pd

def normalize(document):
  scaler = MinMaxScaler()
  document = pd.DataFrame(scaler.fit_transform(document), columns = document.columns)
  return document

def todf(documento):
  document = pd.DataFrame(columns=quimicFeatures)
  document = document.append(documento)
  return document

def pearson(array1, array2) :
  temp = pearsonr(array1,array2)
  return temp[0]

def mean(data):
  return statistics.mean(data)

def concat(df1, df2):
  return pd.concat([df1,df2], ignore_index=True)

def correlation(dataset):
  correlationlist = []
  count_col = dataset.shape[0]
  print(count_col)
  for x in range(count_col):
    static = dataset.iloc[0]
    static = static.to_numpy()
    
    
    dinamic = dataset.iloc[x]
    dinamic = dinamic.to_numpy()

    temp = pearson(static, dinamic)
    correlationlist.append(temp)
  return correlationlist

def fromquerytocrop(crop):
  dataframeCrops = pd.DataFrame(columns=quimicFeatures)
  for x in range(len(crop)):
    
    temp = crop[x]
    dataframeCrops = dataframeCrops.append(temp, ignore_index=True)

  return dataframeCrops[quimicFeatures]

def fromjsontocrop(crop):
  dataFrameCrops = pd.DataFrame(columns=quimicFeatures)
  dataFrameCrops = dataFrameCrops.append(crop, ignore_index=True)
  return dataFrameCrops[quimicFeatures]

quimicFeatures = [ #'pH agua:suelo 2,5:1,0',
                    'fosforo',
                    'aluminio',
                    'calcio',
                    'potasio',
                    'sodio',
                    'zinc']