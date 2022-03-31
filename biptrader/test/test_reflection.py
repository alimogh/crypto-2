""" test_reflection :
    3/31/2022 10:18 AM
    ...
"""
__author__ = "Adel Ramezani <adramazany@gmail.com>"

from unittest import TestCase

def fn1(self,a1,*args,**kargs):
    pass

class TestReflection(TestCase):

    def fn2(self):
        pass

    def test_get_function_name(self):
        print(fn1.__name__)
        print(TestReflection.fn2.__name__)
        print(self.fn2.__name__)