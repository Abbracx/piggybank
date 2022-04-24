from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField
from core.models import Category, Currency, Transaction


class CurrencySerializer(ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id','code','name')


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','name')

class WriteTransactionSerializer(ModelSerializer):
    # currency = SerializerMethodField()
    # category = CategorySerializer()
    currency = SlugRelatedField(slug_field='code', queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ('amount','currency','date','description','category',) 

    # def get_currency(self, instance):
    #     return instance.currency.code



class ReadTransactionSerializer(ModelSerializer):
    # currency = SerializerMethodField()
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = ('id','amount','currency','date','description','category',) 
        read_only_fields = fields

    # def get_currency(self, instance):
    #     return instance.currency.code