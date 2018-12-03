import pathlib as pth
import numpy as np
import pandas as pd
import scipy as sp
import sklearn as skl

file_in = 'data/raw/user_badge_in.csv'

badge_list = pd.read_csv(file_in)

file_out = 'data/processed/user_badge_cluster_with_k_means.csv'

def process_make_user_coordinate(raw):
    ret = raw.groupby(['id', 'name']).max()
    print(raw.sort_values(['id', 'name', 'rank']).head(100).to_string())
    return ret

with open(file_out, mode='w') as f:
    f.write(process_make_user_coordinate(badge_list).to_string())
