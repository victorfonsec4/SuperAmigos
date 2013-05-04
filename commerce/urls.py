from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home', 'commerce.views.home', name='home'),
    url(r'^postar', 'commerce.views.postar', name='postar'),
    url(r'^adicionar', 'commerce.views.adicionar', name = 'adicionar'),
    url(r'^$', 'commerce.views.login', name='login'),
	url(r'^friendlist/$', 'commerce.views.friendlist', name='friendlist'),
    url(r'^adicionar/$', 'commerce.views.adicionar', name='adicionar'),
    url(r'^login2$', 'commerce.views.login2', name = 'login2'), 
    # url(r'^commerce/', include('commerce.foo.urls')),
 	url(r'^deletar', 'commerce.views.deletar', name='deletar'),
    url(r'^deletando', 'commerce.views.deletando', name='deletando'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
