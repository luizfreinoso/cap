from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CAP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('homepage.urls', namespace='homepage')),
    
    # modulos
    url(r'^login/', include('login.urls', namespace='login')),
    url(r'^aps/', include('AP.urls', namespace='aps')),
    
    # recursos
    url(r'^ranexos/', include('RAnexos.urls', namespace='ranexos')),
    url(r'^rhtml/', include('RHTML.urls', namespace='rhtml')),
)