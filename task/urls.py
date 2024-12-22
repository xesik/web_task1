from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
# Страница для добавления новой темы
    path('add_task/', views.new_task, name='add_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.del_task, name='del_task'),
]