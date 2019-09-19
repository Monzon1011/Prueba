from django.conf.urls import patterns, include, url
from App import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^Producto/', views.listarProductos)),
    url(r'^Personas/', views.listarPersonas),
    url(r'^Compras/', views.listarCompra),
)
