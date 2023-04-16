""" lec_pd_groupby.py

Companion codes for the lecture on GroupBy objects
"""

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
df.info()
groups = df.groupby(by='firm')
print(groups)
print(groups.groups)
for firm, idx in groups.groups.items():
    print(f"Data for Firm == {firm}:")
    print("----------------------------------------")
    print(df.loc[idx])
    print("----------------------------------------")
    print("")
for firm, idx in groups.groups.items():
    nobs = len(df.loc[idx])
    print(f"Number of obs for Firm == {firm} is {nobs}")

# Using the apply method
res = groups.apply(len)
print(res)
print(type(res))

for firm, idx in groups.groups.items():
    print(f"pd.isna applied to df[df.firm=='{firm}']:")
    print("----------------------------------------")
    print(pd.isna(df.loc[idx]))
    print("----------------------------------------")
    print("")