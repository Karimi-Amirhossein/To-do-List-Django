from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task
from .forms import TaskForm


class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')


class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/task_list.html'

    def get_queryset(self):
        # Best Practice: Filter tasks for the logged-in user here.
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # The queryset is already filtered, we just add the count.
        context['count'] = context['tasks'].filter(completed=False).count()
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/task_form.html'

    def get_queryset(self):
        # SECURITY FIX: Ensures users can only update their own tasks.
        base_qs = super().get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'tasks/task_confirm_delete.html'

    def get_queryset(self):
        # SECURITY FIX: Ensures users can only delete their own tasks.
        base_qs = super().get_queryset()
        return base_qs.filter(user=self.request.user)