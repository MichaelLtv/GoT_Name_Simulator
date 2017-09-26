import praw
import config
import time
import os
from collections import Counter

import requests


def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "shinobix4's GoT Name Simulator v0.1")
    return r
def get_subreddit_list(f, i):
    user = r.redditor(f)
    subreddit_list = []
    for comment in user.comments.top(limit=None):
        subreddit = comment.subreddit
        subreddit_list.append(subreddit)

    fav_subreddit_list = [subreddit for subreddit, subreddit_count in Counter(subreddit_list).most_common(3)]
    print(fav_subreddit_list)
    return fav_subreddit_list[i]




def run_bot(r, comments_replied_to):
    print("Obtaining 25 comments...")


    for comment in r.subreddit("test").comments(limit = 25):
        if "+/u/GoT_Name_Simulator" in comment.body and comment.id not in comments_replied_to:
            print("String with '+/u/GoT_Name_Simulator' found!")
            comment.reply(comment.author.name + " of the House " + str(get_subreddit_list(comment.author.name, 0)) + ", the First of Their Name, The Unburnt, King of the Shitposters, "
                          "the Lurkers and the First Men, Queen of " + str(get_subreddit_list(comment.author.name, 1)) + ", Khaleesi of the Great " + str(get_subreddit_list(comment.author.name, 2)) + ", Protector "
                          "of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons.")
            print("Replied to comment " + comment.id)

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print(comments_replied_to)

    print("Sleeping for 10 seconds...")
    #Sleep for 10 seconds...
    time.sleep(10)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            #comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)
while True:
    run_bot(r, comments_replied_to)
