from django.urls import path
from django.views import generic
from twitter.views import MainPageView


app_name = 'twitter'  # tutaj dajac app name wzystkie nazwy jak index musza byc poprzedzana nazwa aplikacji(patrz heml
# tak unikniemy nadpisywania nazw

urlpatterns = [
   path('', MainPageView.as_view(template_name='twitter/index.html'),
        name='index'),
]
