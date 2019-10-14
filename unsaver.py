import praw
import time

username = 'name' #Enter your reddit username   
password = 'password' #Enter your reddit password
user_agent = 'app_name' #replace this with your app name
client_id = '**************' # replace this with your 14-char client-id
client_secret = '*************************' #Replace this with your 27-char secret id

keep_nsfw = True #set to true if you want to keep nsfw
keep_non_nsfw = True # set to true if you want to keep anything not nsfw
 
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent + " by /u/" + username,
                     username=username,
                     password=password)

print(reddit.read_only)
print(reddit.user.me())

g = reddit.redditor(username).saved()

print("Starting unsaving")
f= open("removals.txt","a")
f.write("\n")

def to_delete(submission):
    if(submission.over_18 is keep_nsfw):
        return False
    if(submission.over_18 is not keep_non_nsfw):
        return False
    return True

for submission in reddit.redditor(username).saved():
    try:
        if(to_delete(submission)):
            print("unsaving '" + submission.title + "'; URL="+submission.url )
            submission.unsave()
            f.write("unsaving '" + submission.title + "'; URL="+submission.url + "\n")
            time.sleep(1)
        else:
            print("keeping " + submission.title)
    except:
        try:
            if(to_delete(submission)):
                print("unsaving comment under '" + submission.submission.title + "'; URL="+ submission.submission.url)
                submission.unsave()
                f.write("unsaving comment under '" + submission.submission.title + "'; URL="+ submission.submission.url +  "\n")
                time.sleep(1)
            else:
                print("keeping comment under '" + submission.submission.title + "'")
        except:
            print("Could not unsave item with    ID= " + submission.id)
f.close()



