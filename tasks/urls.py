from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, RegisterPage 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', TaskList.as_view(), name='task-list'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
