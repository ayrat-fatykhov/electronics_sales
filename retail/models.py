from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """
    Определяет поля для модели Продукт.
    """
    name = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=255, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Продукт.
        :return: текст с наименованием и моделью Продукта.
        """
        return f'{self.name}, {self.model}'

    class Meta:
        """
        Определяет отображение модели Продукт в админке.
        """
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Link(models.Model):
    """
    Определяет поля для модели Звено.
    """
    CANCEL_DEBT = 0.00

    ELEMENT_CHOICES = (
        ('1', 'Завод'),
        ('2', 'Розничная сеть'),
        ('3', 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='почта', **NULLABLE)
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица', **NULLABLE)
    house_number = models.CharField(max_length=100, verbose_name='номер дома', **NULLABLE)
    element_network = models.CharField(
        max_length=1,
        choices=ELEMENT_CHOICES,
        verbose_name='звено сети'
    )
    products = models.ManyToManyField(Product, verbose_name='продукты')
    provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt = models.FloatField(verbose_name='задолженность перед поставщиком')
    created_to = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)], verbose_name='уровень')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Звено.
        :return: текст с наименованием, звеном сети, продуктами, поставщиком и уровнем иерархией Звена.
        """
        return f'{self.name}, {self.element_network}, {self.products}, {self.provider}, {self.level}'

    class Meta:
        """
        Определяет отображение модели Звено в админке.
        """
        verbose_name = 'звено'
        verbose_name_plural = 'звенья'
