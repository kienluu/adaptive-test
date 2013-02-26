from django.contrib import admin
from adaptive_test.tweet.models import Tweet, TweetUser

admin.site.register(Tweet)
admin.site.register(TweetUser)