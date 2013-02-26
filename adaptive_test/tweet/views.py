from django.views.generic import DetailView
from django.views.generic.list import ListView
from adaptive_test.tweet.models import Tweet


class TweetListView(ListView):
    model = Tweet
    template_name = 'tweet/tweet_list.html'

    def get_queryset(self):
        queryset = super(TweetListView, self).get_queryset()

        if self.request.GET:
            keyword = self.request.GET.get('keyword', None)
            if keyword:
                queryset = queryset.filter(message__contains=keyword)

        return queryset.order_by('sentiment')


class TweetView(DetailView):
    model = Tweet
    template_name = 'tweet/tweet.html'



