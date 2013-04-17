from django.conf.urls.defaults import patterns


urlpatterns = patterns('{{ project_name }}.auth.views',
    (r'^login$', 'django.contrib.auth.views.login', {}, 'login'),
    (r'^logout$', 'django.contrib.auth.views.logout', {}, 'logout'),
    (r'^register$', 'register', {}, 'register')
)
