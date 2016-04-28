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
    words_arr = ["vote", "move", "focus", "arianagrande", "youknowyoulovethem", "sofantastic", "directioners", "onedirection", "arianators", "job", "direction", "beckyg", "break", "sweat", "jobs", "hiring","attack", "found", "snail", "trecru"]
    freq_arr = [0.144034458119, 0.0746667819446, 0.0612551441805, 0.0601417627444, 0.0293148893577, 0.0216741593719, 0.0213447515923, 0.0213357376772, 0.0195082819522, 0.0154183192027, 0.0149060162409, 0.0139231549108, 0.0134837274069, 0.0131880735602, 0.011828392717, 0.0113516388981, 0.0108926781961, 0.0093552115735, 0.0093450981261, 0.00934384501133]

    #code for generating word cloud
    word_count = len(words_arr)
    text = "";
    for i in range(0,word_count):
        for j in range(0,(int)(freq_arr[i]*1000)):
            text = text + words_arr[i] + " "

    tags = make_tags(get_tag_counts(text)[:20], maxsize=100, colors=COLOR_SCHEMES['audacity'])  

    output = os.path.join(os.getcwd(), './static/out')
        
    if not os.path.exists(output):
        os.mkdir(output )            

    create_tag_image(tags, os.path.join(output, 'cloud.png'),
                             size=(500, 333),
                             background=(255, 255, 255, 255),
                             layout=2, fontname='PT Sans Regular')
    return render(request, 'home/index.html', context)


