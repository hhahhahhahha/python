from datetime import time
import numpy as np
import pandas as pd


unames =['user id','age','gender','occupation','zip code']
users =pd.read_csv('C:\\Users\\chenyong\\Desktop\\python文件\\第十二次上机\\ml-100k\\u.user',sep='|',names=unames)
rnames =['user id','item id','rating','timestamp']
ratings=pd.read_csv('C:\\Users\\chenyong\\Desktop\\python文件\\第十二次上机\\ml-100k\\u.data',sep='\t',names=rnames)
users_df=users.loc[:,['user id','gender']]
ratings_df=ratings.loc[:,['user id','rating']]
rating_df = pd.merge(users_df,ratings_df)
print(rating_df.groupby('gender').rating.std())