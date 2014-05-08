from django.conf.urls.defaults import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'/js/(?P<path>.*)$',    'django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/js").replace("\\","/")}),
    url(r'^js/(?P<path>.*)$',    'django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/js").replace("\\","/")}),
    url(r'/images/(?P<path>.*)$','django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/images/").replace("\\","/")}),
    url(r'^images/(?P<path>.*)$','django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/images/").replace("\\","/")}),
    url(r'/css/(?P<path>.*)$',   'django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/css").replace("\\","/")}),
    url(r'^css/(?P<path>.*)$',   'django.views.static.serve',{"document_root":os.path.join(os.path.dirname(__file__),"./templates/css").replace("\\","/")}),
    # Examples:
    # url(r'^$', 'pymonitor.views.home', name='home'),
    # url(r'^pymonitor/', include('pymonitor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('pymonitor.apppymonitor.views',
    #monitor
    url(r'^cluster/$', 'cluster', name='monitor-cluster'),
    url(r'^nodedatacluster/$', 'nodedatacluster', name='nodedatacluster'),
    url(r'^nodedatascluster/$', 'nodedatascluster', name='nodedatascluster'),
    url(r'^clusterhuitu/$', 'clusterhuitu', name='monitor-clusterhuitu'),
    url(r'^clusterhuitu5/$', 'clusterhuitu5', name='monitor-clusterhuitu5'),
    url(r'^clusterhuitu15/$', 'clusterhuitu15', name='monitor-clusterhuitu15'),
    url(r'^memory/$', 'memory', name='memory'),
    url(r'^io/$', 'io', name='io'),
    url(r'^network/$', 'network', name='network'),

    #monitor - sub1
    url(r'^uptime-1/$', 'uptime1', name='monitor-uptime1'),
    url(r'^nodedata/$', 'nodedata', name='nodedata'),
    url(r'^uptime-5/$', 'uptime5', name='monitor-uptime5'),
    url(r'^uptime-15/$', 'uptime15', name='monitor-uptime15'),
    url(r'^uptime-network/$', 'uptimenetwork', name='monitor-uptimenetwork'),
    url(r'^uptime-io/$', 'uptimeio', name='monitor-uptimeio'),
    url(r'^uptime-memory/$', 'uptimememory', name='monitor-uptimememory'),
)
