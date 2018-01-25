#Install praw
import praw
import time

#Paste your credentials in place of "_"
reddit = praw.Reddit(client_id = '_',
                     client_secret = '_',
                     username = '_',
                     password = '_',
                     user_agent = ('_'))

#The program is configured for searching the given word among 999 Titles on askreddit, however, you can change the subreddt by simply typing the name of the sureddit in stead of askreddit.
# You can also adjust the limit to any number you with, the current limit is 999, feel free to change that according to your requirements.

subreddit = reddit.subreddit('Askreddit')

hot_on_Askreddit = subreddit.hot(limit=999)

savefile = open('top_10_on_Askreddit.txt', 'w')
#The proram will save the desired titles with the particular given word on a file named top_10_on_Askreddit.txt (You can also ask for a .csv file
for stuff in hot_on_Askreddit:
#Type the word you want to search in place of "word"
    if "word" in stuff.title:
        savefile.write(stuff.title + "\r\n")
        print(stuff.title)


















































