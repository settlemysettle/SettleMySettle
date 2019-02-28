from django.conf.urls import url
from settle import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
]