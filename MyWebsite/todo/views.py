from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def index(request):
    todos = todo.objects.all()
    context = {"todos": todos}
    return render(request, "todo/index.0.html", context)
