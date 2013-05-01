# -*- coding: utf8 -*-

from Products.CMFCore.utils import getToolByName

from example.gs import logger

_PROPERTIES = [
    dict(name='foo', type_='boolean', value=True),
    dict(name='bar', type_='string', value='xxx'),
]

def registerProperties(context):
    ptool = getToolByName(context, 'portal_properties')
    props = ptool.example_properties
    
    for prop in _PROPERTIES:
        if not props.hasProperty(prop['name']):
            props.manage_addProperty(prop['name'], prop['value'], prop['type_'])
            logger.info("Added missing %s property" % prop['name'])
        else:
            logger.info("Property %s already present. Skipping" % prop['name'])

def registerIndexes(portal):
    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    WANTED_INDEXES = (('getFoo', 'FieldIndex'),
                      )
    indexables = []
    for name, meta_type in WANTED_INDEXES:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s." % (meta_type, name))
        else:
            logger.info("Index %s already found. Skipping" % name)
    # lines below if you want also reindex items when executing it
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s." % ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)

def setupVarious(context):
    if context.readDataFile('example.gs_various.txt') is None:
        return
    portal = context.getSite()
    registerProperties(portal)
    registerIndexes(portal)


def migrateTo1100(context):
    setup_tool = getToolByName(context, 'portal_setup')
    # setup_tool.runImportStepFromProfile('profile-example.gs:default', 'single-step-you-want')
    logger.info('Migrated to version 0.2')
