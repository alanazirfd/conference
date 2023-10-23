from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, attendee, timestamp):
        return (
            six.text_type(attendee.email) + six.text_type(timestamp) +
            six.text_type(attendee.confirmed)
        )
account_activation_token = TokenGenerator()