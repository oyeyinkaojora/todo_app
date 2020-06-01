from django.urls import path
from .views import home,updateTodo,deleteTodo

urlpatterns = [
    path('', home,name = 'home' ),
    path('update-todo/<int:pk>', updateTodo,name = 'update-todo' ),
    path('delete-todo/<int:pk>', deleteTodo,name = 'delete-todo' ),
]