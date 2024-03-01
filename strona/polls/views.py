from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")

def counter(request):
    text_file = open("./templates/counter.html", "r")
    page = text_file.read()
    text_file.close()
    return HttpResponse(page)

def basic(request):
    plik = open("./templates/basic.html", "r")
    strona = plik.read()
    plik.close()
    return HttpResponse(strona)