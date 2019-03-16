from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import CreateView

from twitter import models
from twitter.models import Tweet
from django import forms
from twitter.forms import UserRegisterForm, TweetForm

# Create your views here.


# widok ktory czyta wszystkie tweety, szereguje je po dacie i wrzuca do ctx
class MainPageView(generic.ListView):

    template_name = 'twitter/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.all().order_by('-creation_date')


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = 'twitter/register.html'

    def get(self, request):
        return render(request, 'twitter/register.html',
                     {'form': UserRegisterForm()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})


class ComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
