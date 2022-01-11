from django.urls import path
from .views import NewsList, NewsDetail, CategoryDetail  #, add_like

urlpatterns = [
    # path('', NewsList.as_view(), name='post_list'),
    path('news/', NewsList.as_view(), name='post_list'),
    # path('news/<str:slug>/', NewsDetail.as_view(), name='post_detail'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='post_detail'),  # возможен переход по id статьи\новости
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    # path('like/', add_like, name='add_like'), # не знаю как сделать
]
