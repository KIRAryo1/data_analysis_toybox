import pathlib as pth
import numpy as np
import pandas as pd
import scipy as sp

file_in = 'data/raw/user_badge_in.csv'

badge_list = pd.read_csv(file_in)

file_out = 'data/processed/user_badge_basic_statistics.csv'

with open(file_out, mode='w') as f:
    stat = badge_list['rank'].describe()
    print(stat)
    f.write(stat.to_string())
