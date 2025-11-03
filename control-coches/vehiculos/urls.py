from django.urls import include, path
from . import views

urlpatterns = [
    # Página inicial (Index)
    path('', views.index, name='index'),
    path("__debug__/", include("debug_toolbar.urls")),
]