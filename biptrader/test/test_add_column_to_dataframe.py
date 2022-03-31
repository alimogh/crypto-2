""" test_add_column_to_dataframe :
    3/31/2022 12:05 PM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

import pandas as pd

data={"col1":[1,2,3]
      ,"col2":["a","b","c"]}

df = pd.DataFrame(data)
print(df)

df=df.assign(col3=[4,5,6])
print(df)

df=df.assign(col4=[None]*3)
print(df)

df=df.assign(col5=[None]*len(df))
print(df)
