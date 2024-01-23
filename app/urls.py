from django.urls import path
from .views import hello, content_based_cf, twitter_wordcnt

urlpatterns = [
  path("hello/", hello, name="hello"),
  path('content_based_cf/', content_based_cf),
  path('twitter/', twitter_wordcnt),
]
