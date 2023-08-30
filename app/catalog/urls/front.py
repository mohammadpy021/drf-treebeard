from django.urls import path, include
from catalog.views import front

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', front.CategoryViewSet, basename='front')
app_name = "catalog.front"
urlpatterns = [
    path("", include(router.urls) )
]