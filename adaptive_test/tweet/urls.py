from django.conf.urls import patterns, url
from adaptive_test.tweet.views import TweetListView

urlpatterns = patterns('',
    url(r'', TweetListView.as_view(), name='tweet_tweet_list')
)