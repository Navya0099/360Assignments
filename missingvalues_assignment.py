# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:50:16 2021

@author: NAVYA .P
"""

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/Claimants.csv')

#checking for missing values
x = df.isna().sum()
'''
CASENUM       0
ATTORNEY      0
CLMSEX       12
CLMINSUR     41
SEATBELT     48
CLMAGE      189
LOSS          0
dtype: int64'''

# 4 columns have missing data.we have to Create an imputer object that fills 'Nan' values
# Mean and Median imputer are used for numeric data
# mode is used for discrete data 

#***************CLMSEX*************

sns.boxplot(df.CLMSEX);plt.title('Boxplot');plt.show()
# the boxplot shows no outliers so, mwe can use mean imputer.
# If plot shows any outliers median imputer is best, as mean is influenced by outliers
from sklearn.impute import SimpleImputer

mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
df["CLMSEX"] = pd.DataFrame(mean_imputer.fit_transform(df[["CLMSEX"]]))
C = df["CLMSEX"].isnull().sum()  # all 12 records replaced by mean 

print(C) # 0 missing values


#*****************CLMINSUR*************

sns.boxplot(df.CLMINSUR);plt.title('Boxplot');plt.show()
# the boxplot shows one outlier so, we can use median imputer.
# If plot shows any outliers median imputer is best, as mean is influenced by outliers
from sklearn.impute import SimpleImputer

median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMINSUR"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMINSUR"]]))
d = df["CLMINSUR"].isnull().sum()  # all 41 records replaced by median 

print(d) # 0 missing values

#*****************SEATBELT******************


sns.boxplot(df.SEATBELT);plt.title('Boxplot');plt.show()
# the boxplot shows one outlier so, we can use median imputer.
# If plot shows any outliers median imputer is best, as mean is influenced by outliers
from sklearn.impute import SimpleImputer

median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["SEATBELT"] = pd.DataFrame(median_imputer.fit_transform(df[["SEATBELT"]]))
e = df["SEATBELT"].isnull().sum()  # all 41 records replaced by median 

print(e) # 0 missing values

#*******************CLMAGE********************

sns.boxplot(df.CLMAGE);plt.title('Boxplot');plt.show()
# the boxplot shows one outlier so, we can use median imputer.
# If plot shows any outliers median imputer is best, as mean is influenced by outliers
from sklearn.impute import SimpleImputer

median_imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df["CLMAGE"] = pd.DataFrame(median_imputer.fit_transform(df[["CLMAGE"]]))
f = df["CLMAGE"].isnull().sum()  # all 41 records replaced by median 

print(f) # 0 missing values


y = df.isna().sum()





