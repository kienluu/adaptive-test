# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TweetUser'
        db.create_table('tweet_tweetuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('tweet', ['TweetUser'])

        # Adding model 'Tweet'
        db.create_table('tweet_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tweet.TweetUser'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('followers', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('sentiment', self.gf('django.db.models.fields.FloatField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('tweet', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'TweetUser'
        db.delete_table('tweet_tweetuser')

        # Deleting model 'Tweet'
        db.delete_table('tweet_tweet')


    models = {
        'tweet.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'followers': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sentiment': ('django.db.models.fields.FloatField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tweet.TweetUser']"})
        },
        'tweet.tweetuser': {
            'Meta': {'object_name': 'TweetUser'},
            'handle': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tweet']