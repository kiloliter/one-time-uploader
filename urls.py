from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('djangoapps.myapp.views',
    url(r'^(?P<urlKey>[^/]+)/upload/$', "upload"),
    url(r'^file/(?P<fileKey>[^/]+)/(?P<filename>[^/]+)$', "download"),
    url(r'^createKey/$', "createKey"),
    url(r'^(?P<urlKey>[^/]+)/$', "main"),
)
