from django.conf.urls.defaults import *
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('main.urls')),
    # Examples:
    # url(r'^$', 'ProyectoFinal.views.home', name='home'),
    # url(r'^ProyectoFinal/', include('ProyectoFinal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#agregado abajo
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
#se agrega para el poder registrar 
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    #url(r'^accounts/register/$', 'registration.views.register', {'backend': 'registration.backends.default.DefaultBackend', 'form_class': RegistrationFormUniqueEmail}),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    #url(r'^account/', include('django.contrib.auth.urls')),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
