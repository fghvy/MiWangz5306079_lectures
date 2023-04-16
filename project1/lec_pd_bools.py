""" lec_pd_bools.py

Companion codes for the lecture about selection obs using booleans in Pandas
"""
import pprint as pp

import pandas as pd



data = {
    'date': [
        '2012-02-16 07:42:00',
        '2020-09-23 08:58:55',
        '2020-09-23 09:01:26',
        '2020-09-23 09:11:01',
        '2020-09-23 11:15:12',
        '2020-11-18 11:07:44',
        '2020-12-09 15:34:34',
        ],
    'firm': [
        'JP Morgan',
        'Deutsche Bank',
        'Deutsche Bank',
        'Wunderlich',
        'Deutsche Bank',
        'Morgan Stanley',
        'JP Morgan',
        ],
    'action': [
        'main',
        'main',
        'main',
        'down',
        'up',
        'up',
        'main',
        ],
}
data['date'] = pd.to_datetime(data['date'])
print(type(data['date']))
df = pd.DataFrame(data=data).set_index('date')
print(df)
cond = df.loc[:, 'action'] == 'up' # --> series with dtype: bool
print(cond)
res = df.loc[cond]
print(res)
new_cond = cond.array
res = df.loc[new_cond]
print(res)
print(df.loc[:, [True, False]])
cond = df.loc[:, 'action'] == 'up'
print(df.loc[cond, [False, True]])
print(df.isna())
cond = df.loc[:, 'action'] == 'up'
df['action'][cond] = "UP"
print(df)
cond = df.loc[:, 'action'] == 'UP'
df.loc[cond, 'action'] = 'up'
print(df)
new_df = df.copy()
cond = df.loc[:, 'action'] == 'up'
new_df.loc[cond] = 'UP'
print(new_df)
crit = (df.loc[:, 'action'] == 'up') | (df.loc[:, 'action'] == 'down')
print(df.loc[crit])
crit = df.loc[:, 'action'].str.contains('up|down')
print(df.loc[crit])


data['date'] = pd.to_datetime(data['date'])
print(type(data['date'])) # --> <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# Create the dataframe and set the column 'date' as the index
df = pd.DataFrame(data=data).set_index('date')
print(df)



nba_stats = pd.DataFrame(
    {
        'team':['lakers', 'lakers', 'nets', 'nets', '76ers', '76ers'],
        'player':['lebron', 'davis', 'kyrie', 'durant', 'harden', 'embiid'],
        'ppg':[30,20,29,16,26,28]
    }
)
ser = pd.Series(data=player, index=ppg)
df = pd.DataFrame({''})



















