import pathlib as pth
import numpy as np
import pandas as pd
import scipy as sp
import sklearn as skl

file_in = 'data/raw/user_badge_in.csv'

badge_list = pd.read_csv(file_in)

def process_make_user_coordinate(raw):
    ret = raw.groupby(['id', 'name']).max().reset_index()
    return ret

def badge_similarity(b1, b2):
    if b1.iat[1] != b2.iat[1]:
        return 0
    else:
        return b1.iat[2] * b2.iat[2] / (1 + abs(b1.iat[2] - b2.iat[2]))

u_b = process_make_user_coordinate(badge_list)

def user_similarity(u1, u2):
    sim = 0
    for index1, row1 in u1.iterrows():
        for index2, row2 in u2.iterrows():
            sim += badge_similarity(row1, row2)

    return sim

def get_all_similarities(u_b, f):
    u_b_group_dict = u_b.groupby(['id'])
    user_ids = u_b_group_dict.groups.keys()
    for uid1 in user_ids:
        for uid2 in user_ids:
            if uid1 < uid2:
                u1 = u_b_group_dict.get_group(uid1)
                u2 = u_b_group_dict.get_group(uid2)
                f.write(str(uid1)+', '+str(uid2)+'  '+str(user_similarity(u1, u2))+'\n')

file_out = 'data/interim/badges_sorted_by_users.csv'
with open(file_out, mode='w') as f:
    f.write(process_make_user_coordinate(badge_list).to_string())

file_out = 'data/processed/user_similarities_by_badge.csv'
