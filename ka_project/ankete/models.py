from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=250, unique=True)
    aktiven = models.BooleanField(default=True)
    #dodaj datum, komentar k tekstu
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey('Question')
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class Anketa(models.Model):
    report = {} #sem bo sel pacient, datum izpolnjevanja, list njegovih odgovorov ... to do: #vsi odgovori morajo biti...
