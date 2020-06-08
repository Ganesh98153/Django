from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse, request, HttpResponseRedirect

from Todo.models import TodoList



def viewTodo(request):
    all_todo_list = TodoList.objects.all()

    return render(request, '../templates/index.html', {'all_list': all_todo_list})


def addTodo(request):

    new_todo = request.POST['new_todoList']  #storing new_todoList var from html form file in n
    new__todo = TodoList(task = new_todo)
    new__todo.save()



    return  HttpResponseRedirect('/Todo/')

def deleteTodo(request, Task_Id):

    deleted_todo =  TodoList.objects.get(id = Task_Id)

    deleted_todo.delete()


    return HttpResponseRedirect('/Todo/')


def delete_all_Todo(request):

    temp = TodoList.objects.all()
    temp.delete()

    return HttpResponseRedirect('/Todo/')

