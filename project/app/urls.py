from django.urls import path
from .views import BookListView, CreateBookView, DeleteBookView, UpdateBookView, BookDetailView
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('create/', CreateBookView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateBookView.as_view(), name='update'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
]