from django.contrib import admin

# Register your models here.
from ankete.models import Question, Answer, Anketa

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'aktiven']

class AnswerAdmin(admin.ModelAdmin):
    fields = ['question', 'text']

class AnketaAdmin(admin.ModelAdmin):
    fields = []

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Anketa, AnketaAdmin)
