from django.views.generic import DetailView
from django.views.generic.list import ListView
from adaptive_test.tweet.models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'tweet/tweet_list.html'


class TweetView(DetailView):
    model = Tweet
    template_name = 'tweet/tweet.html'



