from movies import movies, ratings, users
from pathlib import Path
import numpy as np
import matplotlib as plt
import pandas as pd
import chardet

data = pd.merge(pd.merge(ratings, users), movies)
#print(data)

print(data.iloc[:10])

mean_ratings = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5])

