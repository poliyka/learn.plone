# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import learn.plone


class LearnPloneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=learn.plone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'learn.plone:default')


LEARN_PLONE_FIXTURE = LearnPloneLayer()


LEARN_PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LEARN_PLONE_FIXTURE,),
    name='LearnPloneLayer:IntegrationTesting',
)


LEARN_PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LEARN_PLONE_FIXTURE,),
    name='LearnPloneLayer:FunctionalTesting',
)


LEARN_PLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        LEARN_PLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='LearnPloneLayer:AcceptanceTesting',
)
