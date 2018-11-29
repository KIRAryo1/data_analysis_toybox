import pathlib as pth
import numpy as np

file_in = 'data/raw/user_badge_in.csv'

with open(file_in) as f:
    s = f.read()

file_out = 'data/processed/user_badge_out.csv'

with open(file_out, mode='w') as f:
    f.write(s)
