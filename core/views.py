
from rest_framework.generics import  ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from core.models import Category, Currency, Transaction
from core.serializers import CategorySerializer, CurrencySerializer, ReadTransactionSerializer,WriteTransactionSerializer


class CurrencyListAPIView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer 
    pagination_class = None

class CategoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionModelViewSet(ModelViewSet):
    # When having a foreignkey, you should select related
    permission_classes = (IsAuthenticated,)
    # queryset = Transaction.objects.select_related("currency","category", "user")
    # queryset = Transaction.objects.all()
    # serializer_class = TransactionSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ('description','currency__name')
    ordering_fields = ('amount','date',)
    filterset_fields = ("currency__code",)


    # replaced queryset definition above. Done if you want to alter the returned queryset
    def get_queryset(self):
        qs = Transaction.objects.select_related("currency","category", "user").filter(user=self.request.user)
        return qs
    # When you want to alter or customize the serializer_class
    def get_serializer_class(self):
        if self.action in ('list','retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

