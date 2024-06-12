from django.urls import path
from .views import *

urlpatterns = [
    # path('', UserList.as_view(), name='user'),
    path('overdue/', overdue, name='overdue'),
    path('', user_create, name = 'user_insert'),
    path('<int:id>/',user_create, name='user_update'),
    path('delete/<int:id>/', user_delete, name='user_delete'),
    path('list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
]
