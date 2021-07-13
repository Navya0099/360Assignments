# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:25:52 2021

@author: NAVYA .P
"""

import pandas as pd

df = pd.read_csv('C:/Users/NAVYA .P/Desktop/360digitmg_assignments/3rd assignment/DataSets-Data Pre Processing/DataSets/OnlineRetail.csv', encoding= 'unicode_escape')

df.columns
df.dtypes
df.Quantity.dtypes # int64
df.UnitPrice.dtypes  # 'float64'
df.CustomerID.dtypes #float64

# Now we will convert 'int64' into 'float64' type. 
df.UnitPrice = df.UnitPrice.astype('int64') 
df.dtypes



