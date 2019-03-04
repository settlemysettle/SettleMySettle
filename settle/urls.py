from django.conf.urls import url
from settle import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^feed$', views.feed, name="feed"),
    url(r'^upload$', views.upload, name="upload"),
    url(r'^suggest-tag$', views.suggest_tag, name="tags"),
    url(r'^post$', views.post, name="post"),
]