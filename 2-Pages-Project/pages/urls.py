from django.urls import path
from .views import AnasayfaView
from .views import HakkindaView

urlpatterns=[
    path('', AnasayfaView.as_view(),name='anasayfa'),
    path('hakkinda/',HakkindaView.as_view(), name='hakkinda')
]