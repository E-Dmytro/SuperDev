from django.urls import path
from .views import *

urlpatterns = [

    path('', order_create, name = 'order_insert'),
    path('<int:id>/', order_create, name='order_update'),
    path('delete/<int:id>/', order_delete, name='order_delete'),
    path('list/', order_list, name='order_list'),
    path('author_create/', order_create, name='order_create'),
]
