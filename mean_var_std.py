import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')

  listOne = []
  listTwo = []
  listThree = []

  for i in range(3):
    listOne.append(list[i])

  for i in range(3, 6):
    listTwo.append(list[i])

  for i in range(6, 9):
    listThree.append(list[i])

  x = np.array([listOne, listTwo, listThree])

  # find mean list
  axis2Mean = x.mean(axis=1).tolist()
  axis1Mean = x.mean(axis=0).tolist()
  flattenedMean = np.mean(x)
  mean = [axis1Mean, axis2Mean, flattenedMean]
  
  # find variance
  axis2Var = x.var(axis=1).tolist()
  axis1Var = x.var(axis=0).tolist()
  flattenedVar = np.var(x)
  variance = [axis1Var, axis2Var, flattenedVar]

  # find standard deviation
  axis2SD = x.std(axis=1).tolist()
  axis1SD = x.std(axis=0).tolist()
  flattenedSD = np.std(x) # flattened is wrong
  SD = [axis1SD, axis2SD, flattenedSD]

  # find max
  axis2Max = x.max(axis=1).tolist()
  axis1Max = x.max(axis=0).tolist()
  flattenedMax = np.max(x)
  max = [axis1Max, axis2Max, flattenedMax]

  # find min
  axis2Min = x.min(axis=1).tolist()
  axis1Min = x.min(axis=0).tolist()
  flattenedMin = np.min(x)
  min = [axis1Min, axis2Min, flattenedMin]

  # find sum
  axis2Sum = x.sum(axis=1).tolist()
  axis1Sum = x.sum(axis=0).tolist()
  flattenedSum = np.sum(x)
  sum = [axis1Sum, axis2Sum, flattenedSum]

  calculations = {
    "mean": mean,
    "variance": variance,
    "standard deviation": SD,
    "max": max,
    "min": min,
    "sum": sum
  }

  return calculations
