from django.urls import path
from .views import user_profile_view

urlpatterns = [
    path('profilim', user_profile_view, name='profilim') #example.com/kullanicilar/profilim
]