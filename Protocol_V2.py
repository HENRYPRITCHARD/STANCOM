#Setup
import praw, re, csv, random

#Validate Reddit Access
reddit = praw.Reddit(client_id='Dn_ef002ikq0dw',
                     client_secret='B_8gGLkYtz6aDmZ4tkP5Dj3BFIo',
                     password='11365abc',
                     user_agent='pix3lbot_scrape by /u/pix3lbot',
                     username='pix3lbot')
subreddit = reddit.subreddit('pix3lspace')
space = "\n"
sep = "----------"

#Download
def download(channel):
    for submission in subreddit.hot(limit=1000):
        if re.search(channel, submission.title, re.IGNORECASE):
            foreigncomments = {}
            counter = 0
            for top_level_comment in submission.comments:
                comment = top_level_comment.body
                counter = counter + 1
                foreigncomments[counter] = comment + space
            return foreigncomments 

#Sync
def sync(collect,channel):
    foreigncomments = download(channel)
    collect = 0
    for key in foreigncomments:
        with open("localcopy.txt", "a") as fp:
            fp.write(foreigncomments[key])
        collect = collect + 1
    with open("localcopy.txt", "r") as fp:
        counter = 0
        for row in fp:
            counter = counter + 1
    if collect == counter:
        return
    else:
        with open("localcopy.txt", "a") as fp:
            fp.write(foreigncomments[collect])
            print((foreigncomments[collect]))
                    
   
                             
#Perform
def perform(collect,command,prechannel):
    if command == "1":
        channel = input(space)
        sync(collect,channel)
        run(collect,"1n",channel)
    elif command == "2":
        channel == input(space)
    elif command == "1n":
        sync(collect,prechannel)
        run(collect,"1n",prechannel)
    else:
        return


#Run
def run(collect,command,channel):
    if command == "1n":
        perform(collect,command,channel)
    else:
        command = input(space)
        perform(collect,command,0)
    collect = collect + 1
    run(collect,"",channel)
with open("localcopy.txt", "w") as fp:
    fp.write("")
run(0,"",0)
