"""Definition of the ExampleType content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from example.gs import gsMessageFactory as _

from example.gs.interfaces import IExampleType
from example.gs.config import PROJECTNAME

ExampleTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'foo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"New Field"),
            description=_(u"Field description"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ExampleTypeSchema['title'].storage = atapi.AnnotationStorage()
ExampleTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ExampleTypeSchema, moveDiscussion=False)


class ExampleType(base.ATCTContent):
    """An useless example type"""
    implements(IExampleType)

    meta_type = "ExampleType"
    schema = ExampleTypeSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    foo = atapi.ATFieldProperty('foo')


atapi.registerType(ExampleType, PROJECTNAME)
