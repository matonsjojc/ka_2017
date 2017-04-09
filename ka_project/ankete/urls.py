from django.conf.urls import url
from ankete import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'anketa/', views.nova_anketa, name='nova_anketa'),
]
