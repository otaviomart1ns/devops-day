from django.http import HttpResponse

def ola_mundo(request):
    return HttpResponse('Olá Mundo!')

def tdd(request):
    return HttpResponse('Olá TDD!')