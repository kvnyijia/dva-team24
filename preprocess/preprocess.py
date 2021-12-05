import pandas as pd
import numpy as np
import math

# Region
path = '../data/Preprocessed_data.csv'
df4 = pd.read_csv(path)

dfg = df4.groupby(['country', 'isbn', 'img_s', 'img_l', 'book_title']).agg({'user_id': 'count', 'rating': 'mean'})
dfg['log_user_id_cnt'] = dfg['user_id'].apply(lambda x: math.log(x, 2))

user_cnt_max = dfg['log_user_id_cnt'].max()
rating_max = dfg['rating'].max()
dfg['weight'] = dfg[['log_user_id_cnt', 'rating']].apply(lambda x: x[0] / user_cnt_max * 70 + x[1] / rating_max * 30, axis=1)

g = dfg['weight'].groupby('country', group_keys=False)
res = g.apply(lambda x: x.sort_values(ascending=False))
res = res.reset_index()

res.to_csv('../data/region_score_sort.csv')

# Category
df4 = df4.loc[df4['Category'] != '9']
df4['newCategory'] = df4['Category'].apply(lambda x: x[2:-2])

dfcat = df4.groupby(['newCategory']).agg({'user_id': 'count'})
dfcat = dfcat.loc[dfcat['user_id'] > 200]
catList = dfcat.index.tolist()

dfcat = dfcat.reset_index()
dfcat = dfcat.sort_values(by='user_id', ascending=False)
dfcat['log_count'] = dfcat['user_id'].apply(lambda x: math.log(x, 2))
dfcat = dfcat.rename(columns={'user_id': 'count', 'newCategory': 'Category'})

dfcat.to_csv('../data/cat_count_sort.csv', index=False)

df4 = df4.loc[df4['newCategory'].isin(catList)]

dfg = df4.groupby(['newCategory', 'isbn', 'img_s', 'img_l', 'book_title']).agg({'user_id': 'count', 'rating': 'mean'})
dfg['log_user_id_cnt'] = dfg['user_id'].apply(lambda x: math.log(x, 2))

user_cnt_max = dfg['log_user_id_cnt'].max()
rating_max = dfg['rating'].max()
dfg['weight'] = dfg[['log_user_id_cnt', 'rating']].apply(lambda x: x[0] / user_cnt_max * 70 + x[1] / rating_max * 30, axis=1)

g = dfg['weight'].groupby('newCategory', group_keys=False)
res = g.apply(lambda x: x.sort_values(ascending=False))
res = res.reset_index()
res = res.rename(columns={'newCategory': 'Category'})

res.to_csv('../data/cat_score_sort.csv')