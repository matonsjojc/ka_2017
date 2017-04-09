from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'ankete/index.html', context=context_dict)

def nova_anketa(request):
    context_dict = {}
    return render(request, 'ankete/anketa.html', context=context_dict)
