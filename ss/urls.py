from django.conf.urls import patterns, include, url
from django.contrib import admin
from home.views import home_page
from music.views import music_home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ss.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_page),
    url(r'^music/?$', music_home),
)
