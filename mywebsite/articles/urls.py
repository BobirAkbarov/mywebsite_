from django.urls import path
from .views import article_Message_view


urlpatterns = [
    path('', article_Message_view, name='article-homepage'),
    # path('bilim', article_category)
]