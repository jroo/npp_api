from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response
from npp.data.models import Category, Source
import api.handlers
import urllib

def _underscore_to_camelcase(string):
    word_list = string.split('_')
    for i, word in enumerate(word_list):
        word_list[i] = word.capitalize()
    return ''.join(word_list)
    
def _create_query_string(response_get):
    query_dict = {}
    for k,v in response_get.items():
        if v != "":
            query_dict[k] = v

    query_string = '&'.join([k+'='+urllib.quote(str(v)) for (k,v) in query_dict.items()])
    if query_string:
        query_string = "?%s" % query_string
    
    return query_string
    
def index(request):
    categories = Category.objects.all().order_by('title')
    sources = Source.objects.all().order_by('title')
    category_sources = []
    for category in categories:
        cat_sources = Source.objects.filter(category__id=category.id)
        source_list = []
        for s in cat_sources:
            source_list.append({'id':s.id, 'title':s.title})
        this_cat = {'id':category.id, 'sources':source_list }
        category_sources.append(this_cat)
        print category_sources
        
    return render_to_response("data/index.html", {"categories":categories, "sources":sources, "category_sources":category_sources})
    
def result(request, source):
    query_string = _create_query_string(request.GET)
    return HttpResponseRedirect('/api/%s/list.html%s' % (source, query_string))
    
def source_search(request, source):
    try:
        dummy_class = getattr(api.handlers, "%sHandler" % _underscore_to_camelcase(source))
        dummy_obj = dummy_class()
        
        source_info = {}
        source_info["source_name"] = source
        source_info["allowed_keys"] = dummy_obj.get_allowed_keys()
        return render_to_response('data/source_search.html', {'source':source_info})
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def source_select(request):
    return HttpResponseRedirect("/search/%s/" % request.GET['source'])