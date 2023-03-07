from django.shortcuts import render
import praw
from requests.auth import HTTPBasicAuth
import requests
from .models import RedditAPI


def reddit_home(request):
    redall = RedditAPI.objects.all()
    loadRedditApi()
 
    context = {'data': redall}
    return render(request, 'reddit/index.html', context)

def loadRedditApi():
    reddit = praw.Reddit(
        client_id="bOtmWr8d79ph7Z5A-h34BQ",
        username="maw329",
        client_secret="-dLyo2AbHTylLV8xfGpaYHL40JD8ug",
        user_agent="my user agent",
    )

    red = RedditAPI()
 
    for submission in reddit.subreddit("destiny").hot(limit=10): 
        red.title = submission.title
        red.url = submission.url
        red.author = submission.author
        red.author_fullname = submission.author_fullname
        red.domain = submission.domain 
        
        
        print(type(red))
        print(red)
        red.save()
