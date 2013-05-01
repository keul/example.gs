# -*- coding: utf8 -*-

import logging

from zope.i18nmessageid import MessageFactory
from example.gs import config
from example.gs.tool import FooTool

from Products.Archetypes import atapi
from Products.CMFCore import utils

logger = logging.getLogger('example.gs')
gsMessageFactory = MessageFactory('example.gs')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)

#    utils.ToolInit("Foo Tool",
#                   tools=(FooTool,),
#                   icon="qm.gif",
#                   ).initialize(context)
