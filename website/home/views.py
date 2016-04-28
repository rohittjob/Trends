from django.shortcuts import render
from django.http import HttpResponse

from .models import TopHashTags, TopUserMentions

from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from string import Template
import os
import time
import unittest
   
def index(request):
    context = {'hashtags': TopHashTags.objects.order_by('rank'), 'mentions': TopUserMentions.objects.order_by('rank')}

    #array of words with their frequencies
    words_arr = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10", "word11", "word12", "word13", "word14", "word15", "word16","word17", "word18", "word19", "word20", "word21", "word22", "word23", "word24"]
    freq_arr = [0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.1, 0.1, 0.2, 0.01, 0.05, 0.01, 0.01, 0.01, 0.15]

    #code for generating word cloud
    word_count = len(words_arr)
    text = "";
    for i in range(0,word_count):
        for j in range(0,(int)(freq_arr[i]*100)):
            text = text + words_arr[i] + " "

    tags = make_tags(get_tag_counts(text)[:20], maxsize=100, colors=COLOR_SCHEMES['audacity'])  

    output = os.path.join(os.getcwd(), './static/out')
        
    if not os.path.exists(output):
        os.mkdir(output )            

    create_tag_image(tags, os.path.join(output, 'cloud.png'),
                             size=(900, 600),
                             background=(0, 0, 0, 255),
                             layout=LAYOUT_HORIZONTAL, fontname='PT Sans Regular')
    return render(request, 'home/index.html', context)


