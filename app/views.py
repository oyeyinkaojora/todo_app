from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def home(request):
    todos =Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            form.save()
    context = {
        'todos':todos,
        'form':form
    }
    return render(request,'app/home.html',context)      

def updateTodo(request,pk):
    todos_update = Todo.objects.get(id = pk)
    form_update = TodoForm(instance=todos_update)
    if request.method == 'POST':
        form_update = TodoForm(request.POST,instance = todos_update)
        if form_update.is_valid:
            form_update.save()  
            return HttpResponseRedirect('/')
    context = {
        'todo':todos_update,
        'form':form_update,
    }
    return render(request,'app/update.html',context) 

def deleteTodo(request,pk):
    todos_delete =  Todo.objects.get(id = pk)
    todos_delete.delete()
    return redirect('/')
         
