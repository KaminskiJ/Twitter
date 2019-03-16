from django.urls import path
from django.views import generic


app_name = 'twitter'  # tutaj dajac app name wzystkie nazwy jak index musza byc poprzedzana nazwa aplikacji(patrz heml
# tak unikniemy nadpisywania nazw

urlpatterns = [
   path('', generic.TemplateView.as_view(template_name='twitter/index.html'),
        name='index'),  # dajemu tu generyczny template view bo nie ma tu nic specjalnego. Dajemy template name i sie o
]