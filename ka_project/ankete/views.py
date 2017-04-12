from django.core.paginator import Paginator
from django.shortcuts import render
from ankete.models import Anketa, Question, Answer


# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'ankete/index.html', context=context_dict)

def nova_anketa(request):
    anketa = Anketa.objects.create()
    answers = Answer.objects.all()

    #paginator proba - po 2 odgovora na stran
    page = request.GET.get('page', 1) #iz urlja dobi page (?page=2, npr.), ce ne dobi, da default page=1

    paginator = Paginator(answers, 2)

    context_dict = {
        "anketa": anketa,
        "seznam_akt_vprasanj": anketa.seznam_akt_vprasanj(),
        "answers": answers,
        "ans_paginator": paginator.page(page)
    }

    return render(request, 'ankete/anketa.html', context=context_dict)
