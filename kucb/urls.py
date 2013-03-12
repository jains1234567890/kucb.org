from django.conf.urls.defaults import patterns, include, url
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
import kucb.news.views
import kucb.community.views
import kucb.about.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kucb.views.home', name='home'),
    # url(r'^kucb/', include('kucb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^$', kucb.news.views.index),


    url(r'^sitemap\.xml', kucb.news.views.sitemap),
    url(r'^rss/', kucb.news.views.rss),

    url(r'^news/$', kucb.news.views.news),
    url(r'^news/category/(?P<slug>[-\w]+)/$', kucb.news.views.category),
    url(r'^news/article/(?P<slug>[-\w]+)/$', kucb.news.views.article),
    url(r'^post/(?P<slug>[-\w]+)/$', kucb.news.views.post),

    url(r'^community/$', kucb.community.views.community),
    url(r'^community/events/$', kucb.community.views.events),
    url(r'^community/classifieds/$', kucb.community.views.classifieds),
    url(r'^community/add/event/$', kucb.community.views.add_event),
    url(r'^community/events/(?P<slug>[-\w]+)/$', kucb.community.views.event),
    url(r'^community/blotter/$', kucb.community.views.blotter),
    url(r'^blotter/upload/$', kucb.community.views.upload_blotter),

    url(r'^about/$', kucb.about.views.about),
    url(r'^about/people/$', kucb.about.views.people),
    url(r'^about/profile/(?P<slug>[-\w]+)/$', kucb.about.views.profile),
    url(r'^about/program/(?P<slug>[-\w]+)/$', kucb.about.views.program),
    url(r'^about/schedule/$', kucb.about.views.schedule),
    url(r'^about/(?P<slug>[-\w]+)/$', kucb.about.views.about),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
