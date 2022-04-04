from rest_framework import routers

from django.contrib import admin
from django.urls import path
from core import views

router = routers.SimpleRouter()

router.register(r'category', views.CategoryModelViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies')
] + router.urls
