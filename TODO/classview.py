from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from models import *


class TodoListView(ListView):   #todolist_list.html
    model=TodoList
    context_object_name = "list"


class TodoItemList(ListView):
    context_object_name = "itemlist"

    def get_context_data(self, **kwargs):
        context= super(TodoItemList, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    def get_queryset(self):
        k=self.kwargs.get('id')
        if k:
            return TodoItem.objects.all().filter(li_id__exact=k)


class TodoListCreate(CreateView):
    model = TodoList
    fields = ['name','created']
    template_name = 'TODO/todolist_form.html'
    success_url = '/todo/todolist/'


class TodoItemCreate(CreateView):
    model=TodoItem
    fields=['description','duedate','completed','created']
    template_name = 'TODO/todoitem_form.html'

    def form_valid(self, form):
        list_id=self.kwargs.get('id')
        p=TodoList.objects.get(pk=list_id)
        form.instance.li=p
        return super(TodoItemCreate, self).form_valid(form)

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('id') + '/items/'


class TodoListUpdate(UpdateView):
    model = TodoList
    fields = ['name', 'created']
    success_url = '/todo/todolist/'


class TodoItemUpdate(UpdateView):
    model=TodoItem
    fields = ['description','created','duedate','completed']

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('listid') + '/items/'


class TodoListDelete(DeleteView):
    model=TodoList
    success_url = '/todo/todolist/'


class TodoItemDelete(DeleteView):
    model=TodoItem

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('listid') + '/items/'


