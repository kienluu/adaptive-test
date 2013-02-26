from django.conf.urls import patterns, url
from adaptive_test.tweet.views import TweetListView, TweetView

urlpatterns = patterns('',
    url(r'^$', TweetListView.as_view(), name='tweet_tweet_list'),
    url(r'^(?P<pk>[\d]+)/$', TweetView.as_view(), name='tweet_tweet_detail')
)