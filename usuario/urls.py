from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_rest, name='login'),
    url(r'^loginview$', views.login_view, name='loginview')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)