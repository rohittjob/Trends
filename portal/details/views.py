from django.shortcuts import render
from django.http import HttpResponse

from home.models import TopTrends

def detail(request, topic_rank):
	topic_name = TopTrends.objects.get(rank=topic_rank)
	return render(request, 'details/page.html', {'topic_name': topic_name})