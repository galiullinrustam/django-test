from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
class CreateBookView(CreateView):
    model = Book
    template_name = "book-form.html"
    fields = "__all__"
    success_url = reverse_lazy("index")
# Create your views here.
class DeleteBookView(DeleteView):
    queryset = Book.objects.all()
    template_name = "delete.html"
    success_url = reverse_lazy("index")

class UpdateBookView(UpdateView):
    queryset = Book.objects.all()
    fields = "__all__"
    template_name = "book-form.html"
    success_url = reverse_lazy("index")
class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["smile"] = "💋💋💋💋"
        return context