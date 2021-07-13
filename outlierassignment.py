# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:09:06 2021

@author: NAVYA .P
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/boston_data.csv')
sns.boxplot(df.crim);plt.title('Boxplot');plt.show()

#**********crim**********
IQR = df['crim'].quantile(0.75) - df['crim'].quantile(0.25)
lower_limit = df['crim'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['crim'].quantile(0.75) + (IQR * 1.5)
lower_lim = df['crim'].quantile(0.05)
upper_lim = df['crim'].quantile(0.80)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['crim'] > upper_limit, upper_limit, 
                                         np.where(df['crim'] < lower_limit, lower_limit, df['crim'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()

#************indus****************
sns.boxplot(df.indus);plt.title('Boxplot');plt.show()
# no outliers


#**********chas**********

sns.boxplot(df.chas);plt.title('Boxplot');plt.show()

IQR = df['chas'].quantile(0.75) - df['chas'].quantile(0.25)
lower_limit = df['chas'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['chas'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['chas'] > upper_limit, upper_limit, 
                                         np.where(df['chas'] < lower_limit, lower_limit, df['chas'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed

#****************nox**********

sns.boxplot(df.nox);plt.title('Boxplot');plt.show()

# no outliers


#**********rm***********
sns.boxplot(df.rm);plt.title('Boxplot');plt.show()

IQR = df['rm'].quantile(0.75) - df['rm'].quantile(0.25)
lower_limit = df['rm'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['rm'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['rm'] > upper_limit, upper_limit, 
                                         np.where(df['rm'] < lower_limit, lower_limit, df['rm'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()

#outliers are removed

#**********age***********
sns.boxplot(df.age);plt.title('Boxplot');plt.show()
# zero outliers


#************dis************

sns.boxplot(df.dis);plt.title('Boxplot');plt.show()

IQR = df['dis'].quantile(0.75) - df['dis'].quantile(0.25)
lower_limit = df['dis'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['dis'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['dis'] > upper_limit, upper_limit, 
                                         np.where(df['dis'] < lower_limit, lower_limit, df['dis'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed

#************rad************

sns.boxplot(df.rad);plt.title('Boxplot');plt.show()
# zero outliers

#*********tax**************
sns.boxplot(df.tax);plt.title('Boxplot');plt.show()
# zero outliers

#*********ptratio**************
sns.boxplot(df.ptratio);plt.title('Boxplot');plt.show()


IQR = df['ptratio'].quantile(0.75) - df['ptratio'].quantile(0.25)
lower_limit = df['ptratio'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['ptratio'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['ptratio'] > upper_limit, upper_limit, 
                                         np.where(df['ptratio'] < lower_limit, lower_limit, df['ptratio'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed


#*********black**************
#sns.boxplot(df.black);plt.title('Boxplot');plt.show()


IQR = df['black'].quantile(0.75) - df['black'].quantile(0.25)
lower_limit = df['black'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['black'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['black'] > upper_limit, upper_limit, 
                                         np.where(df['black'] < lower_limit, lower_limit, df['black'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed

#*********lstat**************
#sns.boxplot(df.lstat);plt.title('Boxplot');plt.show()


IQR = df['lstat'].quantile(0.75) - df['lstat'].quantile(0.25)
lower_limit = df['lstat'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['lstat'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['lstat'] > upper_limit, upper_limit, 
                                         np.where(df['lstat'] < lower_limit, lower_limit, df['lstat'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed

#*********medv**************
#sns.boxplot(df.medv);plt.title('Boxplot');plt.show()


IQR = df['medv'].quantile(0.75) - df['medv'].quantile(0.25)
lower_limit = df['medv'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['medv'].quantile(0.75) + (IQR * 1.5)

#Replacing outliers
df['df_replaced']= pd.DataFrame(np.where(df['medv'] > upper_limit, upper_limit, 
                                         np.where(df['medv'] < lower_limit, lower_limit, df['medv'])))
#checking the boxplot
sns.boxplot(df.df_replaced);plt.title('Boxplot');plt.show()
#outliers are removed





