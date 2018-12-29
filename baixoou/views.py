from django.shortcuts import render
from .program.downloads import downloads

def download(request):
    data = {}

    url = request.GET.get('url')
    name = request.GET.get('name')
    formato = request.GET.get('format')

    downloads(url,name,formato)

    return render(request, 'baixoou/download.html', data)