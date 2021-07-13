# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:05:11 2021

@author: NAVYA .P
"""

import pandas as pd

df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/animal_category.csv')
df.head(10)

df.drop(['Index'],axis =1,inplace =True)
df.dtypes

df_new = pd.get_dummies(df)


#one hot encoding


from sklearn.preprocessing import OneHotEncoder
# creating instance of one-hot-encoder
enc = OneHotEncoder(handle_unknown='ignore')

enc_df = pd.DataFrame(enc.fit_transform(df).toarray())

# Label Encoding

from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()
X = df.iloc[:]


X['Animals']= labelencoder.fit_transform(X['Animals'])
X['Gender'] = labelencoder.fit_transform(X['Gender'])
X['Homly'] = labelencoder.fit_transform(X['Homly'])
X['Types'] = labelencoder.fit_transform(X['Homly'])

print(X)

