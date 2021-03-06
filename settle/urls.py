from django.conf.urls import url
from settle import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^feed$', views.feed, name="feed"),
    url(r'^upload$', views.upload, name="upload"),
    url(r'^suggest-tag$', views.suggest_tag, name="tags"),
    url(r'^post/(?P<post_id>(\d+))$', views.post, name="post"),
    url(r'^register/$', views.signup, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^account/$', views.account, name="account"),
    url(r'^test/$', views.test, name="test"),

]
