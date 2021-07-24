# -*- coding: utf-8 -*-

from learn.plone import _
from Products.Five.browser import BrowserView
from plone import api


from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Index(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    template = ViewPageTemplateFile('templates/index.pt')
    def __init__(self, request, context):
        self.request = request
        self.context = context

    def __call__(self):
        portal = api.portal.get()
        self.index = portal["index"].listFolderContents()

        # Implement your own actions:
        self.msg = _(u'A small message')
        return self.template()
