from django.shortcuts import render
from django.http import HttpResponse
from home.models import TopHashTags, TopUserMentions
from utilities.live_tweets import *
import json

def detail(request, rank):
    context = {}

    hashtag = TopHashTags.objects.get(rank=rank).hashtag
    context['tsv_name'] = 'topic' + str(rank)
    context['topic_name'] = 'Topic ' + str(rank)

    context['since_id'] = ''
    context['tsv_name'] = 'tsv/' + context['tsv_name'] + '.tsv'
    return render(request, 'details/page.html', context)

def tweet(request):
    keyword = request.GET['keyword']
    try:
        since_id = int(request.GET['since_id'])
    except:
        since_id = None
    tweet = get_tweets(keyword, 1, since_id)
    reply = {}

    if len(tweet) > 0:
        tweet = tweet[0]
        reply['text'] = tweet.text
        reply['dp_url'] = tweet.dp_url
        reply['name'] = tweet.name
        reply['handle'] = tweet.handle
        reply['tweet_id'] = str(tweet.id)
        reply['date'] = tweet.date

    # get_tweets(keyword, 5)
    return HttpResponse(json.dumps(reply),content_type="application/json")
