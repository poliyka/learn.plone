# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from learn.plone.testing import LEARN_PLONE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that learn.plone is properly installed."""

    layer = LEARN_PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if learn.plone is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'learn.plone'))

    def test_browserlayer(self):
        """Test that ILearnPloneLayer is registered."""
        from learn.plone.interfaces import (
            ILearnPloneLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ILearnPloneLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = LEARN_PLONE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['learn.plone'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if learn.plone is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'learn.plone'))

    def test_browserlayer_removed(self):
        """Test that ILearnPloneLayer is removed."""
        from learn.plone.interfaces import \
            ILearnPloneLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ILearnPloneLayer,
            utils.registered_layers())
