import pathlib as pth
import numpy as np
import pandas as pd
import scipy as sp
import sklearn as skl

file_in = 'data/raw/user_badge_in.csv'

badge_list = pd.read_csv(file_in)

file_out = 'data/processed/user_badge_cluster_with_k_means.csv'

def process_make_user_coordinate(raw):
    ret = raw.groupby(['id', 'name']).max().reset_index()
    return ret

def badge_similarity(b1, b2):
    if b1.iat[1] != b2.iat[1]:
        return 0
    else:
        return b1.iat[2] * b2.iat[2] / (1 + abs(b1.iat[2] - b2.iat[2]))

u_b = process_make_user_coordinate(badge_list)
print(badge_similarity(u_b.iloc[1,:], u_b.iloc[5,:]))
print(badge_similarity(u_b.iloc[1,:], u_b.iloc[6,:]))

u1 = u_b[1:5]
u2 = u_b[5:9]

def user_similarity(u1, u2):
    sim = 0
    for index1, row1 in u1.iterrows():
        print(type(row1))
        for index2, row2 in u2.iterrows():
            sim += badge_similarity(row1, row2)

    return sim

print(user_similarity(u1, u2))

with open(file_out, mode='w') as f:
    f.write(process_make_user_coordinate(badge_list).to_string())
