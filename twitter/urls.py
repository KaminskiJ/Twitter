from django import views
from django.urls import path
from twitter.views import MainPageView, RegisterView


app_name = 'twitter'  # tutaj dajac app name wzystkie nazwy jak index musza byc poprzedzana nazwa aplikacji(patrz heml
# tak unikniemy nadpisywania nazw

urlpatterns = [
    path('', MainPageView.as_view(template_name='twitter/index.html'), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
]
