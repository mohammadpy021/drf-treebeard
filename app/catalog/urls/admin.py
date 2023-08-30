from django.urls import path, include
from catalog.views import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', admin.CategoryViewSet, basename='admin')
app_name = "catalog.admin"
urlpatterns = [
    path("", include(router.urls))
]