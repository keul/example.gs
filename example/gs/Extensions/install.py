# -*- coding: utf8 -*-

from zExceptions import BadRequest

from example.gs.interfaces import IFooUtility
from example.gs import logger 

#def install(portal, reinstall=False):
#    # Not needed if you don't need to run different profile conditionally
#    setup_tool = portal.portal_setup
#    setup_tool.runAllImportStepsFromProfile('profile-example.gs:default')
#    logger.info("Installed")

def _removePersistentUtility(portal):
    sm = portal.getSiteManager()
    sm.unregisterUtility(provided=IFooUtility)
    util = sm.getUtility(IFooUtility)
    try:
        del util
        sm.utilities.unsubscribe((), IFooUtility)
        del sm.utilities.__dict__['_provided'][IFooUtility]
        logger.info("Removed utility")
    except KeyError:
        pass

def _removeUserProperty(portal):
    try:
        portal.portal_memberdata.manage_delProperties(['foo'])
        logger.info("User property removed")
    except BadRequest:
        pass

def _removeProperties(portal):
    try:
        portal.portal_properties.manage_delObjects(['example_properties'])
        logger.info("Property sheet removed")
    except BadRequest:
        pass

def _removeTool(portal):
    try:
        portal.manage_delObjects(['portal_foo'])
        logger.info("Portal tool removed")
    except AttributeError:
        pass

def _removeImportStep(portal):
    to_remove = ('example.gs',)
    registry = portal.portal_setup.getImportStepRegistry()
    for step in to_remove:
        if step in registry._registered:
            registry.unregisterStep(step)
            logger.info("Removing import_step %s" % step)

def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-example.gs:uninstall')
        _removeUserProperty(portal)
        _removePersistentUtility(portal)
        _removeProperties(portal)
        _removeTool(portal)
        _removeImportStep(portal)
        logger.info("Uninstall done")
