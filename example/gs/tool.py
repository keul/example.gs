# -*- coding: utf8 -*-

from Globals import InitializeClass
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class FooTool(UniqueObject, SimpleItem): 
    id = 'portal_foo'
    meta_type= 'FooTool' 
    plone_tool = 1 

    def __init__(self):
        self.data_1 = 3
        self.data_2 = 5

    def foo(self):
        self.data_1 += 1
        return self.data_1 + self.data_2

InitializeClass(FooTool)
