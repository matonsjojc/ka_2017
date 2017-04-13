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
    active_questions = Question.objects.all().filter(aktiven=True).order_by('id') #dj se order by id, da gre po vrsti
    report = anketa.report

    #paginator proba - po 2 odgovora na stran
    page = request.GET.get('page', 1) #iz urlja dobi page (2 za "?page=2", npr.), ce ne dobi, da default page=1

    paginator = Paginator(active_questions, 1)
    page_obj = paginator.page(page)
    #odgovori, ki spadajo k vprasanju na pagu:
    related_answers = []
    for a in answers:
        #ce ima a za foreignkej 1. (edino) vprasanje v page_objektu, ga dodaj na seznam related_answers
        if a.question == page_obj[0]:
            related_answers.append(a)



    context_dict = {
        "anketa": anketa,
        "seznam_akt_vprasanj": active_questions,
        "related_answers": related_answers,
        "page_obj": page_obj,
        "report": report
    }

    return render(request, 'ankete/anketa.html', context=context_dict)
