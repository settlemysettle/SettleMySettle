from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class CPasswordValidator(object):
    """Custom validator that makes sure the password is at least 8 characters long and contains at least one digit
    and character."""

    def __init__(self):
        self.min_length = 8
        self.max_length = 30

    def validate(self, password, user=None):
        # Check it contains at least one lowercase char
        if not any(char.islower() for char in password):
            raise ValidationError(
                _('Password must contain at least 1 lowercase letter.'))
        # Check it contains at least one digit
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _('Password must contain at least 1 digit.'))
        # Check it contains at least one uppercase char
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _('Password must contain at least 1 uppercase letter.'))
        # Check it is at least 8 characters long
        if len(password) < self.min_length:
            raise ValidationError(
                _("Password must be at least 8 charaters long"))
        # make sure it isn't too long
        if len(password) > self.max_length:
            raise ValidationError(
                _("Password can only be upto 30 characters.")
            )
