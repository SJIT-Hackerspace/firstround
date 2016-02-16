from django.test import TestCase

# Create your tests here.
from new.models import Contact
...
class ContactTests(TestCase):

    def test_str(self):

        contact = Contact(first_name='admin2', last_name='admin2')

        self.assertEquals(
            str(contact),
            'admin2 admin2',
        )