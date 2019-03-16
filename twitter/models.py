from django.db import models
from django.contrib.auth.models import User

# Create your models here.


TWITTER_MAXIMUM_TWEET_LENGTH = 280


class Tweet(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_TWEET_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # tu dla lepszego printowania
    def __str__(self):
        return f'[{self.creation_date}] ' \
               f'TWEET by {self.author}: {self.content[:20]}'


'''
wersja dla pythona ponizej 3.5
    def __str__(self):
        return '[{}] TWEET by {}: {}'.format(
            self.creation_date,
            self.author, self.content[:20])
'''
