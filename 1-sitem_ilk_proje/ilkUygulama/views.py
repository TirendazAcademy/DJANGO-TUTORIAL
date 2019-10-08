from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def anasayfaView (request):
    return HttpResponse('Merhaba Dünya. Süperrr :)))')