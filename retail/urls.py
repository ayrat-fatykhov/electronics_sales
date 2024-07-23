from django.urls import path

from retail.apps import RetailConfig
from retail.views import LinkCreateView, LinkListView, LinkRetrieveView, LinkUpdateView, LinkDestroyView, \
    ProductCreateView, ProductListView, ProductRetrieveView, ProductUpdateView, ProductDestroyView

app_name = RetailConfig.name


urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/view/<int:pk>/', ProductRetrieveView.as_view(), name='product_view'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDestroyView.as_view(), name='product_delete'),
    path('link/create/', LinkCreateView.as_view(), name='link_create'),
    path('', LinkListView.as_view(), name='link_list'),
    path('link/view/<int:pk>/', LinkRetrieveView.as_view(), name='link_view'),
    path('link/update/<int:pk>/', LinkUpdateView.as_view(), name='link_update'),
    path('link/delete/<int:pk>/', LinkDestroyView.as_view(), name='link_delete'),
]
