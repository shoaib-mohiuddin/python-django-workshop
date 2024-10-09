from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Books

# Create your views here.
class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
       
class BookCreateView(CreateView):
    model = Books
    template_name = 'book_form.html'
    fields = ['title', 'author','description']
    success_url = reverse_lazy('book_list')
