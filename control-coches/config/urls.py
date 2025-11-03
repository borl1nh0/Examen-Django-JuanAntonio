
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls')),
    
]

handler400 = 'vehiculos.views.error_400'
handler402 = 'vehiculos.views.error_402'
handler403 = 'vehiculos.views.error_403'
handler404 = 'vehiculos.views.error_404'
handler500 = 'vehiculos.views.error_500'