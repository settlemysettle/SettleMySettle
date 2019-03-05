from django.test import TestCase
from settle.fields import ColourField
from django.core.urlresolvers import reverse


class ColourFieldTestCase(TestCase):
    def TestIncorrectHexCode(self):
        # Not sure how to test this yet, might need to check how it is used
        # Think I need to use a client to try and select a colour with invalid value

        # Go to home page then navigate to suggest tag, then do stuff?
        # Might be easier to test this when creating a new tag?
        self.client.get(reverse('settle/'))
        response = self.client.get(reverse('settle/suggest-tag'))
