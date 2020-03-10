from unittest import TestCase
from ..Main.Hello import HelloStream
from .Helpers import Helpers

class TestHello(TestCase):
    ARBITRARY_LENGTH = 10

    def test_StringCreation(self):
        targetString = Helpers.randomString(TestHello.ARBITRARY_LENGTH)
        hello = HelloStream(targetString)
        self.assertEqual(str(hello), 'Hello, ' + targetString + '!')
