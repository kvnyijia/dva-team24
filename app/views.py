from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def welcome_view(request):
    return render(request, 'welcome.html')

def selection_view(request):
    return render(request, 'selection.html')

def visualization_view(request):
    return render(request, 'visualization.html')