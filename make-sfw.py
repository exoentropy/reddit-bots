import sys, praw

userAgent = """make-sfw.py (PRAW) // removes posts containing black listed words and phrases // https://github.com/Exoentropy/reddit-bots // /u/Exoentropy"""

reddit = praw.Reddit(userAgent)
reddit.login()

#make black list
blackList = []
for nsfw in sys.stdin:
	blackList.append(nsfw.strip())

#parse user's history and delete posts containing an post from the black list
for post in reddit.user.get_overview(limit = None):
    for nsfw in blackList:
    	if(nsfw in str(post)):
    		post.delete()
