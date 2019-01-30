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

#Collects Foreign Comments
def collect(thread):
    data,i = {},0
    if len(str(thread)) > 3:
        for submission in subreddit.hot(limit=1000):
            if re.search(thread, submission.title, re.IGNORECASE):
                for top_level_comment in submission.comments:
                    i = i + 1
                    data[i] = top_level_comment.body
                return data
    else:
        with open("localcopy.txt", "r") as fp:
            for row in fp:
                i = i + 1
                data[i] = row
            return data

#Create new, unused alias
def newAlias(thread):
    data = collect(thread)
    new  = str.split(data[len(data)], ".")
    return int(new[0]) + 1

#Sends command
def post(content,thread):
    for submission in subreddit.hot(limit=1000):
        if re.search(thread, submission.title, re.IGNORECASE):
            submission.reply(str(newAlias(thread)) + "." + str(content))

##Startup Use## Update Local Copy
def reset(thread):
    with open("localcopy.txt", "w") as fp:
        fp.write("")
    data = collect(thread)
    with open("localcopy.txt", "a") as fp:
        for key in data:
            fp.write(data[key] + space)

#Checks foriegn comments with local comments
def check(thread,data):
    data = collect(thread)
    localdata = collect(1)
    if len(data) != len(localdata):
        print(data[len(data)])
        with open("localcopy.txt", "a") as fp:
            fp.write(data[len(data)] + space)
        return data

#Organizes actions by command
def decode(command,thread):
    if command == "1":
        data = reset(thread)
        while True:
            data = check(thread,data)
    elif command == "2":
        while True:
            content = input(":")
            post(content,thread)
    elif command == "3":
        content = input(":")
        post(content,thread)
    elif len(command) == 5:
        navigate(command)

#Locate a post 
def navigate(thread):
    options = collect(thread)
    for key in options:
        print(options[key])    
    thread = input(":")
    #for submission in subreddit.hot(limit=1000):
        #if re.search(thread, submission.title, re.IGNORECASE):
            #submission.reply(".poll" + space)
    command = input(":")
    decode(command,thread)

navigate("54325")




