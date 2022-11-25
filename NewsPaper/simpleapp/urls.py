from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, NewDetail, NewCreate, NewUpdate, NewDelete, Search

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='new_list'),
   path('search/', Search.as_view(), name='news_search'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewDetail.as_view(), name='new_detail'),
   path('create/', NewCreate.as_view(), name='new_create'),
   path('<int:pk>/update/', NewUpdate.as_view(), name='new_update'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
]