from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
urlpatterns = [
    # Examples:
    url(r'^$', 'new.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', 'new.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bfs.txt/','new.views.a',name='a'),
     url(r'^feed/','new.views.feed',name='feed'),
     url(r'^home/','new.views.home',name='home'), 
      url(r'^get/','new.views.get',name='get'),
      url(r'^quest.json/','new.views.quest',name='quest'),
      url(r'^bye/','new.views.bye',name='bye'),
      url(r'^/sub/test.json/','new.views.test',name='test'),
      url(r'^logint/','new.views.logint',name='logint'),
      url(r'^validate/','new.views.validate',name='validate'),
      url(r'^sub/','new.views.sub',name='sub'),
      url(r'^register', 'new.views.register', name='register'),
      url(r'^sub/result.json/','new.views.res',name='res'),
]

