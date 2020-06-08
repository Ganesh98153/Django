from django.urls import path
from . import views


urlpatterns = [
    path('',views.viewTodo),
    path('addTodo/', views.addTodo),
    path('Todo/',views.viewTodo),
    path('deleteTodo/<int:Task_Id>/', views.deleteTodo),
    path('delete_all_Todo/',views.delete_all_Todo),

]
