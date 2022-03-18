from asyncio.windows_events import NULL
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import pearsonr
import statistics
import numpy as np
import pandas as pd

from plantainApp.models import PlantainTypes

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

def correlation(dataset, n):
  correlationlist = []
  count_col = dataset.shape[0]

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



def fromquerytoptype(type):
  dataframetypes = pd.DataFrame(columns=plantainType)
  for x in range(len(type)):
    temp = type[x]
    dataframetypes = dataframetypes.append(temp, ignore_index=True)
  
  return dataframetypes[plantainType]




def fromjsontocrop(crop):
  dataFrameCrops = pd.DataFrame(columns=quimicFeatures)
  dataFrameCrops = dataFrameCrops.append(crop, ignore_index=True)
  return dataFrameCrops[quimicFeatures]




def maxelements(list1, N):
  final_list = []
  
  for i in range(0, N): 
    max1 = 0
          
    for j in range(len(list1)):     
      if list1[j] > max1:
        max1 = list1[j]
                  
    list1.remove(max1)
    final_list.append(max1)
  
  return final_list



def datatolist(document):
  listob = []
  shape = document.shape[0]

  for i in range(shape):
    static = document.iloc[i]
    static = static.to_numpy()
    listob.append(static)
  
  return listob

def type(crop):

  newcrop = pd.DataFrame()
  newcrop['fosforo'] = crop['fosforo']
  newcrop['potasio'] = crop['potasio']
  newcrop['calcio'] = crop['calcio']

  types = PlantainTypes.objects.values()
  types = fromquerytoptype(types)
  print(types)

  newtypes = pd.DataFrame()
  newtypes['fosforo'] = types['fosforo']
  newtypes['potasio'] = types['potasio']
  newtypes['calcio'] = types['calcio']


  document = pd.DataFrame()
  document = newcrop.append(newtypes, ignore_index=True)


  top = correlation(document, 1)
  return top



def toobjecttofloat (document, columns):
  for column in columns:
    document[column] = pd.to_numeric(document[column], errors='coerce')



def cleanData (document, replaceValue, value):
  document.replace(to_replace = replaceValue , value= value, inplace=True )



quimicFeatures = [ #'pH agua:suelo 2,5:1,0',
  'fosforo',
  'aluminio',
  'calcio',
  'potasio',
  'sodio',
  'zinc']
            
plantainType = ['phMin', 'nitrogeno', 'fosforo', 'potasio', 'calcio']