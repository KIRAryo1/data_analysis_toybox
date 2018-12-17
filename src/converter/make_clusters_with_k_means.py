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

def 

def centroid_user_distance(cent, user):
    dist = 0
    for index1, row1 in cent.iterrows():
        for index2, row2 in u2.iterrows():
            sim += badge_similarity(row1, row2)

    return sim

