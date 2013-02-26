import urllib2
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import simplejson
from adaptive_test.tweet.models import Tweet, TweetUser


class Command(BaseCommand):
    help = "Pull in tweets from a api add/update them in the database"

    # 2012-09-27T16:15:41Z
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def main(self):
        response = urllib2.urlopen(
            'http://adaptive-test-api.herokuapp.com/tweets.json')
        tweet_list = simplejson.loads(response.read())
        assert type(tweet_list) is list
        for tweet_dict in tweet_list:
            tweet_dict['created_at'] = datetime.strptime(
                tweet_dict['created_at'], self.DATE_FORMAT)
            tweet_dict['updated_at'] = datetime.strptime(
                tweet_dict['updated_at'], self.DATE_FORMAT)

            user, created = TweetUser.objects.get_or_create(
                handle=tweet_dict['user_handle'])

            tweet_args = {
                'created_at': tweet_dict['created_at'],
                'updated_at': tweet_dict['updated_at'],
                'message': tweet_dict['message'],
                'sentiment': tweet_dict['sentiment'],
                'followers': tweet_dict['followers'],
                'user': user
            }

            tweet_model, created = Tweet.objects.get_or_create(
                id=tweet_dict['id'], defaults=tweet_args)


    def handle(self, *args, **options):
        max_tries = 2
        for attempt_num in range(1, max_tries + 1):
            try:
                if self.main():
                    break
            except Exception as e:
                print 'There was an error in the update_tweet command.\n\n' \
                      'error: %s' % e