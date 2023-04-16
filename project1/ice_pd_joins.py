""" lec_pd_joins.py

Companion codes for the lecture on combining pandas objects
"""

import pandas as pd

dates = [
  '2020-01-02',
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600,
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

ser = pd.Series(data=prices, index=dates)
# Data Frame with close and bday columns
df = pd.DataFrame({'close': ser, 'bday': bday})
print(df)


ones_by_datas = pd.Series(1,index= dates)
print(ones_by_datas)



print(df + ones_by_datas)



ones_by_cols = pd.Series(1, index=['bday','close'])
print(ones_by_cols)

left = pd.DataFrame(
        data=[('L1'), ('L2'), ('L3')],
        index=[1,2,3],
        columns=['L'],
        )
print(left)
right = pd.DataFrame(
        data=[('R3'), ('R4'), ('R5')],
        index=[3,4,5],
        columns=['R'],
        )
print(right)
print(left.join(right, how='left'))
print(left.join(right, how='inner'))
print(left.join(right, how='outer'))





