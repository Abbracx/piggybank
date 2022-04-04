from rest_framework.serializers import ModelSerializer
from core.models import Category, Currency


class CurrencySerializer(ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id','code','name')


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','name')