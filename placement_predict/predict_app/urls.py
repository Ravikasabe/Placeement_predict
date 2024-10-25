from django.urls import path 
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('index/', index, name='index'),
    path('result/', predict_view, name='result'),
    path('jobrole/', jobrole, name='jobrole'),
    path('apply/', apply, name='apply'),
    path('send_email/', send_email, name='send_email'),
]