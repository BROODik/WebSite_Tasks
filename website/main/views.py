from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    task = Task.objects.order_by('completed','created_on')
    return render(request, 'index.html', {'title':'Главная страница', 'tasks':task})

def about(request):
    return render(request, 'about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не заполнена"
    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'create.html', context)
