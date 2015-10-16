from django.shortcuts import render
from django.http import HttpResponse

from .models import TopTrends

def index(request):
	topics_list = TopTrends.objects.order_by('rank')
	context = {'topics_list': topics_list}
	return render(request, 'home/index.html', context)

def detail(request, topic_rank):
    return HttpResponse("Details of topic with rank %s." % topic_rank)