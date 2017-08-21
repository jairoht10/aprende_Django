from django.conf.urls import url
from .views import LiceoCreate, LiceoList
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(LiceoList.as_view()), name='liceo_lista'),
    url(r'^registro$', login_required(LiceoCreate.as_view()), name='liceo_registro'),
]