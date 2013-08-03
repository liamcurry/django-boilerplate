from django.conf.urls.defaults import patterns


urlpatterns = patterns('{{ project_name }}.auth.views',
    (r'^signin$', 'signin', {'template_name': 'auth/signin.html'}, 'signin'),
    (r'^logout$', 'logout', {}, 'logout'),
    (r'^register$', 'join', {}, 'join')
)
