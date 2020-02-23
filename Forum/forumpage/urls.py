from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('db', views.putindb, name='putindb'),
    # path('', views.forum, name='forum'),
    url(r'^forumpage/(?P<roomID>.+)/',views.homepage, name='homepage'),
    url(r'^forumpage/',views.homepageRedirect, name='homepageRedirect'),
    url(r'^db',views.get_post_list.as_view(), name='indb'),
    url(r'^room', views.createRoom.as_view(), name='createRoom')
]



# forumpage/roomID