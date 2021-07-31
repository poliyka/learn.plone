# -*- coding: utf-8 -*-

from learn.plone import _
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Index(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('templates/index.pt')
    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.template()
