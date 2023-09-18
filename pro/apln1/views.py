from django.shortcuts import render
from django.http import HttpResponse
from apln1.models import book
# Create your views here.
def home(request):
    return HttpResponse ("hello hello")

def work1(request):
    return render(request,"work1.html")

def data(request):
    k= book.objects.all()
    return render (request, "list.html", {"b":k})