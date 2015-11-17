from django.shortcuts import render
from django.http import HttpResponse

from .models import TopHashTags, TopUserMentions


def index(request):
    context = {'hashtags': TopHashTags.objects.order_by('rank'), 'mentions': TopUserMentions.objects.order_by('rank')}
    return render(request, 'home/index.html', context)
