import praw
import pandas as pd

#from config import cid, csec, ua

#create a reddit connection
reddit = praw.Reddit(client_id= cid,
                     client_secret= csec,
                     user_agent= ua)
