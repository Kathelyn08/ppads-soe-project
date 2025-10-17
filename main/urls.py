from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudos/', include('estudos.urls')),
    path('', RedirectView.as_view(url='/estudos/login/', permanent = False))
]