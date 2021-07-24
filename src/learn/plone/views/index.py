# -*- coding: utf-8 -*-

from learn.plone import _
from Products.Five.browser import BrowserView
from plone import api


from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Index(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('templates/index.pt')
    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.template()


class IndexTest(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('templates/index_test.pt')
    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'Index test')
        return self.template()


class SubPage(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('templates/subpage.pt')
    def __call__(self):
        # Implement your own actions:
        self.msg = _(u'subpage')
        return self.template()
