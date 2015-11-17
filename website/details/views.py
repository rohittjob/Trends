from django.shortcuts import render
from django.http import HttpResponse

from home.models import TopHashTags, TopUserMentions


def detail(request, type, rank):
	context = {}
	if type == 'h':
		hashtag = TopHashTags.objects.get(rank=rank).hashtag
		context['tsv_name'] = 'H_' + hashtag[1:].lower()
		context['topic_name'] = hashtag

	else:
		mention = TopUserMentions.objects.get(rank=rank).mentioned_user
		context['tsv_name'] = 'M_' + mention[1:].lower()
		context['topic_name'] = mention

	context['tsv_name'] = 'tsv/' + context['tsv_name'] + '.tsv'
	
	return render(request, 'details/page.html', context)
