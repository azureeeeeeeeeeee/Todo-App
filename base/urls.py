from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('logout', views.logoutPage, name='logout'),

    path('', views.home, name='home'),

    path('add-item', views.createTodo, name='add-item'),

    path('done/<str:pk>', views.doneTodo, name='done-item'),
    path('failed/<str:pk>', views.failedTodo, name='failed-item'),
    path('task/<str:pk>', views.detailTask, name='detail-task'),

    path('edit-item/<str:pk>', views.editTask, name='edit-task'),   
    path('delete/<str:pk>', views.delete, name='delete-task'),   

]
