from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'orcamentos/home.html')

def control_panel(request):
    return render(request, 'orcamentos/panel.html')

