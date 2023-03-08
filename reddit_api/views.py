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
    for post in reddit.subreddit("destiny").hot(limit=10):
        posts.append({
            'title': post.title,
            'url': post.url,
            'score': post.score,
            'author': post.author.name,
        })
   
    
    context = {'data': posts}
    return render(request, 'reddit/index.html', context)
    return JsonResponse({'posts': posts})

