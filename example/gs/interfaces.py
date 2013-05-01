# -*- coding: utf8 -*-

from zope.interface import Interface
from zope import schema

from example.gs import gsMessageFactory as _

class IExampleGSLayer(Interface):
    """Marker interface for the example.gs product layer"""


class IFooUtility(Interface):
    pass

    def do():
        pass


class IExampleType(Interface):
    """An useless example type"""

    foo = schema.TextLine(
        title=_(u"New Field"),
        required=False,
        description=_(u"Field description"),
    )
