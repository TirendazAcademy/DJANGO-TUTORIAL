from django.urls import path
from .views import AnaSayfaView

urlpatterns=[
    path('', AnaSayfaView.as_view(), name='anasayfa')
]