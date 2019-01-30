#Setup
import praw,re

#Validate Reddit Access
reddit = praw.Reddit(client_id='Dn_ef002ikq0dw',
                     client_secret='B_8gGLkYtz6aDmZ4tkP5Dj3BFIo',
                     password='11365abc',
                     user_agent='pix3lbot_scrape by /u/pix3lbot',
                     username='pix3lbot')

subreddit = reddit.subreddit('pix3lspace')
space = "\n"
sep = "----------"




def collect(post,local,fp):
    data,i = {},0
    if local == 1:
        with open("localcopy.txt", "r") as fp:
            for row in fp:
                data[i] = row[0:len(row)-1]
                i = i + 1
            return data
    elif local == 0:
        for comment in post.comments:
            data[i] = comment.body
            i = i + 1
        return data

def newAlias(post):
    data = collect(post,0,0)
    new  = str.split(data[len(data)-1], ".")
    return int(new[0]) + 1

def reset(post,fp):
    with open("localcopy.txt", "w") as fp:
        fp.write("")
    data = collect(post,0,fp)
    with open("localcopy.txt", "a") as fp:
        for key in data:
            fp.write(data[key] + space)

def check(post,fp):
    data = collect(post,0,fp)
    localdata = collect(post,1,fp)
    if len(data) != len(localdata):
        print(data[len(data)-1])
        with open("localcopy.txt", "a") as fp:
            fp.write(data[len(data)-1] + space)
        

def decode(oldthread,thread,command,post,fp):
    reset(post,fp)
    if command != "pull":
        post.reply(str(newAlias(post)) + "." + str(command))
        print("sent")
        connect(oldthread,thread,2)
    elif command == "pull":
        while True:
            for post in subreddit.hot(limit=1000):
                if re.search(thread, post.title, re.IGNORECASE):
                    check(post,fp)
            
def connect(oldthread,thread,step):
    post = ""
    with open("localcopy.txt", "r") as fp:
        for post in subreddit.hot(limit=1000):
            if re.search(thread, post.title, re.IGNORECASE):
                #select thread
                if step == 0:
                    options = collect(post,0,fp)
                    for i in options:
                        print(options[i])
                    connect(thread,input(":"),1)
                #load selected thread
                elif step == 1:
                    decode(oldthread,thread,input(":"),post,fp)
                #reload subreddit, save selected thread
                elif step == 2:
                    connect(thread,oldthread,3)
                #shuffle into selected thread
                elif step == 3:
                    connect(thread,oldthread,1)
               
                    

                    

connect("","54325",0)
