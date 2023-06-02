from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from my_todo.models import Todo


class TodoList(ListView):
    model = Todo
    print("Hello")


class ToDoCreate(CreateView):
    model = Todo
    fields = ['title', 'description', 'created_date', 'state']
    success_url = reverse_lazy('todo_list')


class TodoUpdate(UpdateView):
    model = Todo
    fields = ['title', 'description', 'created_date', 'state']
    success_url = reverse_lazy('todo_list')


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
