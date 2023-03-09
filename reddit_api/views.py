from django.shortcuts import render
import praw
from requests.auth import HTTPBasicAuth
import requests
from .models import RedditAPI
from django.http import JsonResponse

def reddit_home(request):
    redall = RedditAPI.objects.all()
    reddit = praw.Reddit(
        client_id="bOtmWr8d79ph7Z5A-h34BQ",
        username="maw329",
        client_secret="-dLyo2AbHTylLV8xfGpaYHL40JD8ug",
        user_agent="my user agent",
    )

    posts = []
    for post in reddit.subreddit("mrgirlreturns").new(limit=50):
        posts.append({
            'title': post.title,
            'url': post.url,
            'score': post.score,
            'author': post.author.name,
            'ups': post.ups,
            'permalink': post.permalink,
        })
   
    context = {'data': posts[2::]}
    return render(request, 'reddit/index.html', context)
    #return JsonResponse({'posts': posts})

