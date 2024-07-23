from django.contrib import admin
from django.db.models import QuerySet

from retail.models import Link, Product

admin.site.register(Product)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    Отображает в админке некоторые элементы Звена.
    Реализует возможности фильтрации Звеньев по городу и обнуление задолженности перед поставщиком.
    """
    list_display = ('name', 'element_network', 'provider', 'debt', 'level')
    list_filter = ('city',)
    actions = ('cancel_debt',)

    @admin.action(description='Обнулить задолженость')
    def cancel_debt(self, request, qs: QuerySet):
        qs.update(debt=Link.CANCEL_DEBT)
