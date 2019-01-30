#Setup
import praw, re, csv, random


#Validate Reddit Access
reddit = praw.Reddit(client_id='Dn_ef002ikq0dw',
                     client_secret='B_8gGLkYtz6aDmZ4tkP5Dj3BFIo',
                     password='zzzzzz',
                     user_agent='pix3lbot_scrape by /u/pix3lbot',
                     username='pix3lbot')
subreddit = reddit.subreddit('pix3lspace')
space = "\n"
sep = "----------"


#Download 
def download(code):
    for submission in subreddit.hot(limit=1000):
        if re.search(code, submission.title, re.IGNORECASE):
            b = {}
            counter = 0
            for top_level_comment in submission.comments:
                comment = top_level_comment.body
                counter = counter + 1
                b[counter] = comment
            return b


#Fetch
a = {}
v = ""
def fetch(code):
    a = download(code)
    for key in a:
        v = a[key]
        print(v)


#Upload
def create(code,data):
    for submission in subreddit.hot(limit=1000):
        if re.search(code, submission.title, re.IGNORECASE):
            submission.reply(str(data))


#Watch Channel
c = {}
def probe(code,location):
    c = download(code)
    for key in c:
        print("down: " + c[key + location])
        with open("ProbeData.txt", 'r') as fp:
            counter = 1
            for row in fp:
                if row != c[counter]:
                    print("save: " + row)
                    with open("ProbeData.txt", 'a') as fp:
                        fp.write(c[counter] + space)
                elif row == c[counter]:
                    print("Up to date")
                counter = counter + 1
                probe(code,counter)
            

    
    
                
        


#Controller
def split(status):
    if status == "Download":
        name = input("File Location:" + space)
        fetch(name)
    elif status == "New Command Line":
        name = input("Command Channel:" + space)
    elif status == "Create":
        name = input("File Location:" + space)
        data = input("Content:" + space)
        create(name,data)
    elif status == "Probe":
        name = input("Command Channel:" + space)
        with open("ProbeData.txt", 'w') as fp:
            fp.write(sep + space)
        probe(name,0)
    else:
        print("Command Not Recognized")


    
    
    



    
#Run Loop
def run():
    status = input(space)
    split(status)
    run()
    
run()




    



    
        

                
