import pathlib as pth
import numpy as np
import pandas as pd
import scipy as sp
import sklearn as skl

file_in = 'data/raw/user_badge_in.csv'

badge_list = pd.read_csv(file_in)

def process_make_user_coordinate(raw):
    return raw.groupby(['id', 'name']).max().reset_index()

def process_make_language_list(raw):
    return raw['name'].unique()

languages = process_make_language_list(badge_list)

NUMBER_OF_CLUSTER = 10
MAX_INITIAL_BADGE_LEVEL = 15

def generate_centroid_seed(languages):
    matrix = np.random.rand(NUMBER_OF_CLUSTER, len(languages)) * MAX_INITIAL_BADGE_LEVEL
    return pd.DataFrame(matrix, columns=languages)

centroid_seed = generate_centroid_seed(languages)

def centroid_user_distance(cent, user):
    for index_c, row_c in cent.iterrows():
        sum_c = 0
        for index1, row1 in user.iterrows():
            # print(np.sqrt(sum((cent[row1['name']] - row1['rank'])**2)))
            sum_c += (row_c[row1['name']] - row1['rank'])**2

        print(index_c, np.sqrt(sum_c))

    return 0

def user_groupby(u_b):
    return u_b.groupby(['id'])

def user_ids(u_b):
    return u_b.groupby(['id']).groups.keys()

def user_badge_fill_with_zero(user, languages):
    df = pd.DataFrame(columns=languages)
    df.loc[user.loc[0]['id']] = 0
    return df


u_b = process_make_user_coordinate(badge_list)
uids = user_ids(u_b)
# print(user_groupby(u_b).get_group(1))
print(user_groupby(u_b).get_group(1))
print(user_badge_fill_with_zero(user_groupby(u_b).get_group(1), languages))
# print(centroid_seed)
#
# centroid_user_distance(centroid_seed, user_groupby(u_b).get_group(1))

