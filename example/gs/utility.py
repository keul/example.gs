# -*- coding: utf8 -*-

from zope.interface import implements
from .interfaces import IFooUtility

class FooUtility(object):
    implements(IFooUtility)

    def do(self):
        print "Do something"
