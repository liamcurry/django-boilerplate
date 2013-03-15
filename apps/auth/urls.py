from django.conf.urls.defaults import patterns


urlpatterns = patterns('apps.auth.views',
    (r'^login/$', 'login', {}, 'login'),
    (r'^logout/$', 'logout', {}, 'logout'),
    (r'^signup/$', 'signup', {}, 'signup')
)
