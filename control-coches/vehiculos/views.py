from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, Sum, Avg
#from .models import Marca, Fabrica, ITV, Coche, Revision

def error_400(request, exception=None):
    return render(request, 'errores/400.html', None, None, 400)

def error_402(request, exception=None):
    return render(request, 'errores/402.html', None, None, 402)

def error_403(request, exception=None):
    return render(request, 'errores/403.html', None, None, 403)

def error_404(request, exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def error_500(request, exception=None):
    return render(request, 'errores/500.html', None, None, 500)

