from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField
from core.models import Category, Currency, Transaction
from django.contrib.auth.models import User


class CurrencySerializer(ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id','code','name')

class ReadUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        read_only_fields = fields

class CategorySerializer(ModelSerializer):

    user = ReadUserSerializer()
    class Meta:
        model = Category
        fields = ('id','name', 'user')

class WriteTransactionSerializer(ModelSerializer):
    # currency = SerializerMethodField()
    # category = CategorySerializer()
    currency = SlugRelatedField(slug_field='code', queryset=Currency.objects.all())
    class Meta:
        model = Transaction
        fields = ('amount','currency','date','description','category',) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields['category'].queryset = user.categories.all()

    # def get_currency(self, instance):
    #     return instance.currency.code



class ReadTransactionSerializer(ModelSerializer):
    # currency = SerializerMethodField()
    currency = CurrencySerializer()
    category = CategorySerializer()
    user = ReadUserSerializer()

    class Meta:
        model = Transaction
        fields = ('id','amount','currency','date','description','category','user') 
        read_only_fields = fields

    # def get_currency(self, instance):
    #     return instance.currency.code