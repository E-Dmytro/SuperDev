from django.urls import path
from .views import *

urlpatterns = [
    # path('', AuthorList.as_view(), name='employee'),
    path('', author_create, name = 'author_insert'),
    path('<int:id>/',author_create, name='author_update'),
    path('delete/<int:id>/', author_delete, name='author_delete'),
    path('list/', author_list, name='author_list'),
    path('employee_create/', author_create, name='author_create'),
]
