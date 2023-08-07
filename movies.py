import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib as plt
import chardet

#create pandas table for usernames
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, engine='python',
names=unames)

print(users[:5])

#Create pandas table for ratings
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, engine='python',
names=rnames)

print(ratings[:5])


mnames = ['movie_id', 'title', 'genres']

# Detect file encoding
with open('movies.dat', 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']

# Read the file with the detected encoding for 
movies = pd.read_table('movies.dat', sep='::', header=None, engine='python', encoding=encoding, names=mnames)
print(movies[:5])

#merge pandas tables
data = pd.merge(pd.merge(ratings, users), movies)
#print(data)

#print first 10 rows of merged table
print(data.iloc[:10])

#print mean of table the rows are average ratings and the columns sort by gender
mean_ratings = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5])

#group gender in terms of rating, for the movies below 250 in ratings
ratings_by_title = data.groupby('title').size()
active_title = ratings_by_title.index[ratings_by_title >= 250]
print(active_title)

#print ratings where titles are the index
mean_ratings = mean_ratings.loc[active_title]
print(mean_ratings)

#print movies sorted by highest rated movies by females
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:4])

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
sorted_by_diff[:15]

sorted_by_diff[::-1][:15]

# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
print(rating_std_by_title)

