from django.test import TestCase
from .models import *
from .state_machine import change_state

class TestState(TestCase):
    def test_invalid(self):
        user = User.objects.create(username="u", role="merchant")
        s = KYCSubmission.objects.create(user=user, state="approved")

        with self.assertRaises(Exception):
            change_state(s, "draft")