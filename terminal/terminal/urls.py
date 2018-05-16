"""terminal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
import classifieds.views as views
from django.conf.urls import  include, url



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^createnewpost',views.posting, name = 'newPost'),
    url(r'^signup', views.signup, name = 'signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^classHome', views.classHome, name = 'classHome'),
    url(r'^viewallpostings',views.viewposts, name = 'viewposts'),
    url(r'^post/(\d+)/$', views.viewpost, name='post'),
    url (r'^myposts/$', views.viewMyPost, name = 'myposts'),
    url(r'^forumMain', views.forumsMainPage, name = 'mainForums'),
    url('^forum/(?P<string>[\w\-]+)/$', views.forumAPCPage, name = 'apcPage'),
    url('^forum/(?P<string>[\w\-]+)/newTopic', views.forumNewTopic, name = 'newTopic'),
    url(r'^forumPost/(\d+)/$', views.viewForum, name='post'),
    url(r'^reply/(\d+)/$', views.postReply, name='reply'),
    url('^classified/(?P<string>[\w\-]+)/$', views.viewAPCPosts, name = 'apcClass'),
    url('^classified/(?P<string>[\w\-]+)/(?P<cater>[\w\-]+)', views.viewcaterPosts, name = 'caterClass'),
    url('^forum/(?P<string>[\w\-]+)/(?P<cater>[\w\-]+)', views.catergoryOrg, name = 'caterView'),
    url(r'^home', views.home, name = 'home'),
    url('^hub/(?P<string>[\w\-]+)/$', views.viewAPCHub, name = 'apcHub'),
    url('^extras/(?P<string>[\w\-]+)/$', views.apcExtras, name = 'apcExtra'),
    url('^extras/(?P<string>[\w\-]+)/(?P<cater>[\w\-]+)', views.apcExtrasC, name = 'apcExtraC'),



]
