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
    return ret

def badge_similarity(b1, b2):
    if b1.index[0][1] != b2.index[0][1]:
        return 0
    else:
        return b1.iat[0,0] * b2.iat[0,0] / (1 + abs(b1.iat[0,0] - b2.iat[0,0]))

u_b = process_make_user_coordinate(badge_list)
print(u_b[1:20])
print(badge_similarity(u_b[1:2], u_b.iloc[6:7]))




with open(file_out, mode='w') as f:
    f.write(process_make_user_coordinate(badge_list).to_string())
