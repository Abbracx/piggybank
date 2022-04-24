
from rest_framework.generics import  ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Category, Currency, Transaction
from core.serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer,WriteTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer 

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionModelViewSet(ModelViewSet):
    # When having a foreignkey, you should select related
    queryset = Transaction.objects.select_related("currency","category")
    # queryset = Transaction.objects.all()
    # serializer_class = TransactionSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ('description','currency__name')
    ordering_fields = ('amount','date',)
    filterset_fields = ("currency__code",)

    # When you want to alter or customize the serializer_class
    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

