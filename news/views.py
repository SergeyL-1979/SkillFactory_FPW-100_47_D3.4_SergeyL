from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Comment, Category, PostCategory


class NewsList(ListView):
    """ Вывод из базы данных всех постов. Так же сортировка по дате, от самой свежей новости до старой
    с помощью ordering = ['-create_date'].
    paginate_by - позволяет выводить указанное количество постов на страницу """
    model = Post
    context_object_name = "post_list"
    ordering = ['-create_date']
    paginate_by = 5

    """ get_context_data() - Этот метод используется для заполнения словаря для использования в качестве контекста 
    шаблона. Например, ListViews заполнит результат из get_queryset() как object_list. Вероятно, вы будете чаще 
    всего переопределять этот метод, чтобы добавлять объекты для отображения в ваших шаблонах. """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['category_name'] = Category.objects.all()
        return context


class NewsDetail(DetailView):
    """ Выводим полностью все данные поста: заголовок поста, дату его создания, сам текст поста, автора поста,
    рейтинги поста и автора. Так же тут видим и комментарии к этому посту, автора комментария и рейтинг комментария. """
    model = Post
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(comment_post=self.kwargs['pk'])
        context['post_category'] = PostCategory.objects.get(post=self.kwargs['pk']).category
        return context


class CategoryDetail(DetailView):
    """ Выводим список категорий. Далее фильтруем посты по категориям и делаем вывод всех постов
    относящихся к данной категории. """
    model = Category
    context_object_name = 'category_detail'

    def get_context_data(self, **kwargs):
        id = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        " Контекст для списка постов в текущей категории. "
        context['category_news'] = Post.objects.filter(post_category=id)
        " Контекст постов данной категории. "
        context['post_category'] = PostCategory.objects.get(post=self.kwargs['pk']).category
        return context

# ============= Реализация повышения рейтинга =================================
# def add_like(request):
#     if request.POST:
#         pk = request.POST.get('pk')
#         post = Post.objects.get(id=pk)
#         post.like()
#         # post.postAuthor.update_rating()
#     return redirect(request.META.get('HTTP_REFERER'))
