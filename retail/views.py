from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from retail.models import Link, Product
from retail.serializers import LinkSerializer, LinkUpdateSerializer, ProductSerializer
from users.permissons import IsActive


class ProductCreateView(generics.CreateAPIView):
    """
    Отвечает за создание Продукта
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductListView(generics.ListAPIView):
    """
    Отвечает за отображение списка Продуктов
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductRetrieveView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одного Продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateView(generics.UpdateAPIView):
    """
    Отвечает за редактирование Продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductDestroyView(generics.DestroyAPIView):
    """
    Отвечает за удаление Продукта
    """
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class LinkCreateView(generics.CreateAPIView):
    """
    Отвечает за создание Звена
    """
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActive]


class LinkListView(generics.ListAPIView):
    """
    Отвечает за отображение списка Звеньев
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class LinkRetrieveView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одного Звена
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class LinkUpdateView(generics.UpdateAPIView):
    """
    Отвечает за редактирование Звена
    """
    serializer_class = LinkUpdateSerializer
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class LinkDestroyView(generics.DestroyAPIView):
    """
    Отвечает за удаление Звена
    """
    queryset = Link.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
