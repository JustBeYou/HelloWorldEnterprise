from random import choices
from string import ascii_uppercase

class Helpers:
    @staticmethod
    def joinWithEmptySeparator(string):
        return ''.join(string)

    @staticmethod
    def randomUpperCaseList(length):
        return choices(ascii_uppercase, k = length)

    @staticmethod
    def randomString(length):
        return Helpers.joinWithEmptySeparator(Helpers.randomUpperCaseList(length))