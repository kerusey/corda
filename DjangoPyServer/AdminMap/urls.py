from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import CoffeeBreakerSpot

urlpatterns = [
    url(r'', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'data.geojson$', GeoJSONLayerView.as_view(model=CoffeeBreakerSpot, properties=('name', 'xCoord', 'yCoord')), name='data')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
