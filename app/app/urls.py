from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'product', views.ProductViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
