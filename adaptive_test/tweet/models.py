import re
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.db import models


class TweetUser(models.Model):
    handle = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        # Django does not perform the cleaning methods automatically
        # when saving:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#validating-objects
        # So we need to manually call this as we will be saving these models in
        # code ourselves.
        self.full_clean()
        super(TweetUser, self).save()


class Tweet(models.Model):
    user = models.ForeignKey(TweetUser)
    message = models.CharField(
        max_length=255, validators=[MinLengthValidator(1)])
    followers = models.PositiveIntegerField()
    sentiment = models.FloatField(
        validators=[MinValueValidator(-1.0), MaxValueValidator(1.0)])

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(TweetUser, self).save()


