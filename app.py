import praw
import pandas as pd
from pprint import pprint

from config import cid, csec, ua

#create a reddit connection
reddit = praw.Reddit(client_id= cid,
                     client_secret= csec,
                     user_agent= ua)

subreddits_titles = ["news", "worldnews", "science", "coronavirus"]

for sub in subreddits_titles:
	subreddit = reddit.subreddit(sub).top(limit=1)

	for post in subreddit:
		pprint(vars(post))
