import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ka_project.settings')

import django
django.setup()

from ankete.models import Anketa, Question, Answer
