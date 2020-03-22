import praw
import pandas as pd
import dash_table

from pprint import pprint

from config import cid, csec, ua

#create a reddit connection
reddit = praw.Reddit(client_id= cid,
                     client_secret= csec,
                     user_agent= ua)

#chosen ubreddits
subreddits_titles = ["news", "worldnews", "science", "coronavirus"]


#list for df converstion
posts = []

#return important attributes
def post_attributes(post):
    posts.append([post.title, post.score, post.num_comments, post.selftext,
                  post.created, post.pinned, post.total_awards_received])


#return attributes top posts in subreddits of interest
for sub in subreddits_titles:
     subreddit = reddit.subreddit(sub).top(limit=1)

     for post in subreddit:
        #pprint(vars(post))
        print(post.title)
        print(post.score)
        print(post.num_comments)
        print(post.selftext)
        print(post.created)
        print(post.total_awards_received)

        #call attributes function
        post_attributes(post)


#create a dataframe
posts_df = pd.DataFrame(posts, columns=['title', 'score', 'comments', 'post',
                                       'created', 'pinned', 'total awards'])

#return top 3 df rows
posts_df.head(3)


##gauge word density in each post
#copy df
df = posts_df.copy()

#count words in post
df['words']=df['post'].apply(lambda x: len(x.split()))

#count characters in post
df['chars'] = df['post'].apply(lambda x: len(x.replace(" ","")))

#calculate word density
df['word density'] = (df['words'] / (df['chars'] +1 )).round(3)

#count unique words
df['unique words'] = df['post'].apply(lambda x: len(set(w for w in x.split())))

#percent of unique words
df['unique density'] = (df['unique words'] / df['words']).round(3)


#use dash to make dashboard layout pwetty
layout = dash_table.DataTable(
    id='table',
    columns=[{"name":i,"id": i} for i in df.columns],
    data=df.to_dict('records')
)
