from django.shortcuts import render


def index(request):
    index_hello = 'Hello world!!!'
    context = {'index_hello': index_hello}
    return render(request, 'index.html', context)
