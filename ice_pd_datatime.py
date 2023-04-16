import os
import datetime as dt

import pandas as pd

import toolkit_config as cfg


CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')




start = dt.datetime(year = 2022 , month = 12 , day = 31, hour = 0)
delta = dt.datetime(hours = 12)
end = start + delta
print(start)
print(end)




x = dt.datetime(2023, 12, 31, 9, 30, 33)
delta = dt.datetime(year = 2023)
result = x.strftime



print(prc.loc[:, 'dataframe'])
x = dt.datetime(15,3,2019)
result = x.strftime("%d trading day in %m %Y")
print(result)










