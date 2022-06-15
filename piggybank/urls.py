from rest_framework import routers

from django.contrib import admin
from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()

router.register(r'category', views.CategoryModelViewSet, basename='category')
router.register(r'transaction', views.TransactionModelViewSet, basename='transaction')

urlpatterns = [
    path('login/', obtain_auth_token, name='obtain-auth-token'),
    path('admin/', admin.site.urls),
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies')
] + router.urls
