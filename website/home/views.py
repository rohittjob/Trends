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

    text = "Somewhat abcd abcd abcd abcd abcd surprisingly, a simple low-level hack made a tremendous difference: when hack constructing the sprite I compressed pixels blocks of 32 1-bit pixels into 32-bit integers, thus reducing hack the number of checks (and memory) by 32 times.";
    tags = make_tags(get_tag_counts(text)[:30], maxsize=120, colors=COLOR_SCHEMES['audacity'])
    data = create_html_data(tags, (450,300), layout=LAYOUT_HORIZONTAL, fontname='PT Sans Regular')
        
    template_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates/home/template.html'), 'r')    
    html_template = Template(template_file.read())
        
    tags_template = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; height: %(height)dpx;"><a class="tag %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
    left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; line-height:%(lh)dpx;">%(tag)s</a></li>'
        
    context['tags'] = ''.join([tags_template % link for link in data['links']])
    context['width'] = data['size'][0]
    context['height'] = data['size'][1]
    context['css'] = "".join("a.%(cname)s{color:%(normal)s;}\
    a.%(cname)s:hover{color:%(hover)s;}" % 
                                  {'cname':k,
                                   'normal': v[0],
                                   'hover': v[1]} 
                                 for k,v in data['css'].items())
        
    html_text = html_template.substitute(context)
        
    html_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates/home/index.html'), 'w')
    html_file.write(html_text)
    html_file.close()       

    return render(request, 'home/index.html', context)
