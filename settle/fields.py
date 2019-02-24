import re # use a regular expression to validate a colour field

from django.db import models
from django.core.validators import RegexValidator # can validate a hex code using a regular expression

colour_re = re.compile('^#([A-Fa-f0-9]{6})$') # only matches hex codes of # + six hex digits
validate_colour = RegexValidator(colour_re, 'Please enter a valid colour', 'invalid')


class ColourField(models.CharField):
    # we define a new custom field to hold tag colours
    # It's stored as a string, so it extends from CharField
    
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 18
        return super(ColourField, self).__init__(*args, **kwargs)
