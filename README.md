# reddit-clear-saved-posts
This allows you to clear your saved posts on reddit with an option to keep posts marked nsfw/not-nsfw

Before running, you need to create an application [here.](http://www.reddit.com/prefs/apps/)

## Setup

When creating your app, you need:
 * a name
 * to select the "Script" radiobutton labelled "Script for personal use. Will only have access to the developers accounts"
 * set your redirect uri to "http://localhost:8080"
 
![Application config](https://cdn.discordapp.com/attachments/479969158021251083/633280007418019846/unknown.png)

In the Python script you need to change a couple of variables:
You can also find your app's information by going [here](http://www.reddit.com/prefs/apps/) and expanding your app by clicking "edit".

|Parameter   | Value                |
|:----------:|:--------------------:|
|`username`    | Your reddit username |
|`password`    |Your reddit login password|
|`user_agent`|Your application's name|
|`client_id`|Your 14-char app-ID|
|`client_secret`|Your app's 27-char authorization key|

Lastly, you can change the values of `keep_nsfw` and `keep_non_nsfw` to your liking.

## Executing

In order for this to work, you need to have [Python](https://www.python.org/downloads/) installed alongside with the [praw module](https://pypi.org/project/praw/).
Finally, you can execute the program by navigating to the location of the script in your command prompt and typing "python unsaver.py"
It will start going through your saved posts and write all unsaved posts to a `removals.txt` file in the same directory.

## Further info

I used praw 6.4.0 and Python 3.7.3
