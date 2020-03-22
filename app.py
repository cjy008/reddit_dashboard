import praw
import pandas as pd
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
