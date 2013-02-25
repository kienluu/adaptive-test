import re
from django.core.validators import RegexValidator

tweet_user_regex = RegexValidator(
    re.compile(r'@[a-z0-9_\-]+', re.IGNORECASE),
    u'Enter a valid user handle',
    'invalid'
)