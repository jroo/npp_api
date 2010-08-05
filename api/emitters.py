from django.template.loader import render_to_string
from piston.emitters import Emitter
import re

def get_page_info(request):
    csv_path = request.META['PATH_INFO'].replace('.html', '.csv')
    xml_path = request.META['PATH_INFO'].replace('.html', '.xml')
    json_path = request.META['PATH_INFO'].replace('.html', '.json')
    
    if "page" in request.GET:
        page_num = int(request.GET['page'])
    else:
        page_num = 1
    next_page = page_num + 1
    
    query_string = "?%s" % request.META['QUERY_STRING']
    print query_string
    query_string_no_page = "%s" % re.sub('page\=\d+', '', query_string)
    print query_string_no_page      
    
    if page_num > 1:
        prev_page = page_num - 1
    else:
        prev_page = None
    
    return { 'csv_path':csv_path, 'xml_path':xml_path, 'json_path':json_path, 'page_num':page_num, 
        'prev_page':prev_page, 'next_page':next_page, 'query_string':query_string, 'query_string_no_page':query_string_no_page}
    
def construct_to_list(construct):
    data = []
    header_row = []
    for key, value in construct[0].items():
        header_row.append(key)
    
    for row in construct:
        this_row = []
        for header in header_row:
            this_row.append(row[header])
        data.append(this_row)
    return { 'header_row':header_row, 'data':data }
    
class HTMLEmitter(Emitter):
    def render(self, request):
        page_info = get_page_info(request)
        data = construct_to_list(self.construct())
        return render_to_string("api/data_html_view.html", { 'page_info':page_info, 'data':data })

Emitter.register('html', HTMLEmitter, 'text/html')