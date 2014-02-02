from django.conf.urls import patterns, include, url
from polls import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vote.views.home', name='home'),
    # url(r'^vote/', include('vote.foo.urls')),

    #url(r'^$', views.index, name='index'),
    url(r'^tedy-vote/(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^tedy-vote/(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^tedy-vote/(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^tedy-vote/(?P<poll_id>\d+)/add_choice/$', views.add_choice, name='add_choice'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
