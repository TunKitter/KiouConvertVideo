from django.urls import path
from . import views
urlpatterns = [
    path("convertVideo",views.convert_to_m3u8),
]