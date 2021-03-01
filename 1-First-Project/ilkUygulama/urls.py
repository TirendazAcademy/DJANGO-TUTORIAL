from django.urls import path
from .views import anasayfaView

urlpatterns= [
    path('', anasayfaView, name="anasayfa")
]