from django.conf.urls import include, url, patterns
from django.contrib import admin
#from link1 import views
from django.conf import settings
#urlpatterns = [
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = patterns('',
#                       url(r'^index/$', views.index),
                       url(r'^admin/', admin.site.urls),
                      
#                       url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'app_info.html'}),
                       #url(r'app-info/?','app.views.Login'),
                       url(r'^$','app.views.Login'),
                       url(r'app-logout/?', 'app.views.Logout'),
                       #url(r'app-user/?', 'app.views.Users'),
                       url(r'app-one/?','app.views.One'),
                       url(r'accounts/profile/?', 'app.views.One'),
                       url(r'app-im/?', 'app.views.Create'),
                       url(r'index/(\d*)/?', 'app.views.Index'),
                       url(r'app-close/(\d*)/?', 'app.views.Close'),
                       url(r'media/(?P<path>.*)?', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT},),
                       )
