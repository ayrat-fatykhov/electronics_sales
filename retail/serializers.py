from rest_framework import serializers

from retail.models import Link, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность.
    """
    class Meta:
        """
        Определяет какие поля класса Продукт будут сериализованы.
        """
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность.
    """
    class Meta:
        """
        Определяет какие поля класса Звено будут сериализованы.
        """
        model = Link
        fields = '__all__'


class LinkUpdateSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность.
    Исключает изменение поля "задолженность перед поставщиком".
    """
    class Meta:
        """
        Определяет какие поля класса Звено будут сериализованы.
        """
        model = Link
        exclude = ['debt']
