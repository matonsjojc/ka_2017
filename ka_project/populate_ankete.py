import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ka_project.settings')

import django
django.setup()

from ankete.models import Anketa, Question, Answer

def populate():

    questions = [
        {"text": "tole je vprašanje 1",
         "aktiven": True,
         "answers": [
             "1.odg. na 1. vpr.",
             "2. odg. na 1. vpr.",
             "3. odg. na 1. vpr."
             ]},
        {"text": "Vprašanje 2 je tole.",
         "aktiven": True,
         "answers": [
             "1.odg. na 2. vpr.",
             "2. odg. na 2. vpr.",
             "3. odg. na 2. vpr."
             ]},
        {"text": "3., (po defaultu neaktivno) vprašanje",
         "aktiven": False,
         "answers": [
             "1.odg. na 3. vpr.",
             "2. odg. na 3. vpr.",
             "3. odg. na 3. vpr."
             ]}
    ]

    for q in questions:
        add_question(q["text"], q["aktiven"])
        print("adding question: ", q["text"], q["aktiven"])
        for a in q["answers"]:
            add_answer(a, q["text"])
            print("adding answer:", a)

def add_question(text, aktiven):
    q = Question.objects.get_or_create(text=text, aktiven=aktiven)[0]
    q.save()
    return q

def add_answer(answer_text, question_text):
    q = Question.objects.get(text=question_text)
    a = Answer.objects.get_or_create(text=answer_text, question=q)
    return a

#start execution here
if __name__ == '__main__':
    print("Starting population script...")
    populate()
