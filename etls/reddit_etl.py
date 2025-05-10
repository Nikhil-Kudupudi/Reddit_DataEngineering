import os

import praw
from praw import Reddit
def connect_reddit(client_id,client_secret,user_agent)-> Reddit:
    try:
        reddit=praw.Reddit(client_id=client_id,
                           client_secret=client_secret,
                           password="",
                           user_agent=user_agent)
        print("connected to reddit")
        return reddit 
    except  Exception as e:
        raise Exception(e)
def extract_posts(reddit_instance:Reddit,subreddit:str,time_filter:str,limit=None):
    try:
        subreddit=reddit_instance.subreddit(subreddit)
        posts=subreddit.top(time_filter=time_filter,limit=limit)
        post_lists=[]
        
        print(posts)
    except Exception as e:
        raise Exception(e)