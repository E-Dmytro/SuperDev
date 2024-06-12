from django.urls import path
from .views import *

urlpatterns = [
    path('', book_form, name='book_insert'),
    path('list/', BookListAll.as_view(), name='list_all'),
    #path('<int:book_id>/', by_id, name='by_id'),
    path('<int:id>/', book_form, name='book_update'),
    path('delete/<int:id>/', book_delete, name='book_delete'),
    path('unordered/', unordered, name='unordered'),
    path('book_list/', BookListSearch.as_view(), name='book_list'),

]
