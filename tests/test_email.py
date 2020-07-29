from unittest import TestCase
from functions.email import is_correct_email


class EmailFunctioinTestCAse(TestCase):
    def test_email1(self):
        self.assertTrue(is_correct_email("masteraalish@gmail.com"))

    def test_email2(self):
        self.assertFalse(is_correct_email("mfwfwrwgmail.com"))

    def test_email(self):
        self.assertTrue(is_correct_email("wfwrf@gmail.com"))

