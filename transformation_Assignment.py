# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:19:36 2021

@author: NAVYA .P
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/Calories_consumed.csv')


# checking the boxplot and histogram

plt.hist(df.Weight_gained) #histogram

sns.boxplot(df.Weight_gained);plt.title('Boxplot');plt.show() #boxplot


# checking skewness
df.Weight_gained.skew() #1.2557366483972048

#Fchecking kurtosis
df.Weight_gained.kurt() #0.4312724433726336

#applying logartithm
df['weight_base10'] = np.(df['Weight_gained'])
print(df)

df.weight_base10.skew() # 0.36064224197129063
#Skewness is decreased to 0.36

df.weight_base10.kurt() # -1.1215243221757696
#kurtosis is decreased to negative value.

# so considering another transformation method of the column

df['weight_Squareroot']=df['Weight_gained']**(1/1.25)
df
df.weight_Squareroot.skew() #1.1022048818875132

df.weight_Squareroot.kurt() #-0.018259172023545656

#****************Calories_Consumed****************

plt.hist(df.Calories_Consumed) #histogram

sns.boxplot(df.Calories_Consumed);plt.title('Boxplot');plt.show() #boxplot


# checking skewness
df.Calories_Consumed.skew() # 0.6549299573588712

#Fchecking kurtosis
df.Calories_Consumed.kurt() #-0.29048129735135975

#applying logartithm
df['calories_base10'] = np.log(df['Calories_Consumed'])
print(df)

df.calories_base10.skew() # 0.1619823036541557
#Skewness is decreased to 0.16

df.calories_base10.kurt() # -0.9901699454643298
#kurtosis is decreased to negative value.

# so considering another transformation method of the column

df['calories_Squareroot']=df['Calories_Consumed']**(1/1.25)
df
df.calories_Squareroot.skew() #0.5528324344161623

df.calories_Squareroot.kurt() #-0.4821146664899314

