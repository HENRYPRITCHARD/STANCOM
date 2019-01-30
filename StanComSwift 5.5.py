#Setup
import praw,re

#Validate Reddit Access
reddit = praw.Reddit(client_id='Dn_ef002ikq0dw',
                     client_secret='B_8gGLkYtz6aDmZ4tkP5Dj3BFIo',
                     password='zzzzzz',
                     user_agent='pix3lbot_scrape by /u/pix3lbot',
                     username='pix3lbot')

subreddit = reddit.subreddit('pix3lspace')
space = "\n"
sep = "----------"

def collect(post,local,fp):
    data,i = {},0
    if local == 1:
        for row in fp:
            data[i] = row[0:len(row)-1]
            i = i + 1
        return data
    elif local == 0:
        for comment in post.comments:
            data[i] = comment.body
            i = i + 1
        return data

def check(dataO,dataL):
    if len(dataO) != len(dataL):
        disc = len(dataO) - len(dataL)
        for i in range(disc): 
            with open("localcopy.txt", "a") as fp:
                fp.write(dataO[len(dataO)-disc+i] + space)
                print(dataO[len(dataO)-disc+i])

def decode(bypass,thread,command,dataO,dataL,post):
    if command != "pull":
        post.reply(str(command))
        connect(bypass,thread,0)
    elif command == "pull":
        check(dataO,dataL)
        connect(bypass,thread,1)

def connect(bypass,thread,skip):
    with open("localcopy.txt", "r") as fp:
        if len(bypass) != 0:
            for post in subreddit.hot(limit=1000):
                if re.search(bypass, post.title, re.IGNORECASE):
                    dataO = collect(post,0,fp)
                    if skip == 0:
                        decode(bypass,thread,input(":"),dataO,dataO,post)
                    else:
                        dataL = collect(post,1,fp)
                        decode(bypass,thread,"pull",dataO,dataL,post)
        else:
            for post in subreddit.hot(limit=1000):
                if re.search(thread, post.title, re.IGNORECASE):
                    options = collect(post,0,fp)
                    for i in options:
                        print(options[i])
                    connect(input(":"),thread,0)
                
                   
                    
                    






connect("","54325",0)
