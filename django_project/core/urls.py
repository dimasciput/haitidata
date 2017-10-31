from django.contrib import admin
from geonode.sitemap import LayerSitemap, MapSitemap

import autocomplete_light

autocomplete_light.autodiscover()
admin.autodiscover()

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('geonode',)
}

sitemaps = {
    "layer": LayerSitemap,
    "map": MapSitemap
}
from osgeo_importer.urls import urlpatterns as importer_urlpatterns

from geonode.urls import *

urlpatterns = patterns(
    '',
    url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),
    url(r'^', include('geonode.urls')),
    url(r'^chart/', include('charts_app.urls')),
    url(r'^table/', include('wfs_harvest.urls')),
    url(r'^clip/', include('clip-and-ship.urls')),
    url(r'^tutorials/$', TemplateView.as_view(template_name='tutorials.html'), name='tutorials'),
)
urlpatterns += patterns(
    '',
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += importer_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
