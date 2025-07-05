# urls.py
from core.urls import urlpatterns as core_urls

urlpatterns = [
    path('api/', include(core_urls)), 
