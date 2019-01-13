from django.shortcuts import render
from django.http import HttpResponse
from .forms import RgistrationForm

def index(request):
    form = RgistrationForm()
    context = {'myregistrationform':form}
    return render(request,'firstapp/register.html',context=context)

# Create your views here.
