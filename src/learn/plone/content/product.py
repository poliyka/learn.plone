# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer


from learn.plone import _


class IProduct(model.Schema):
    """ Marker interface and Dexterity Python Schema for Product
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('product.xml')

    title = schema.TextLine(
        title=_(u'Title'),
        required=True
    )

    description = schema.Text(
        title=_(u'description'),
        required=False
    )

    thumb = namedfile.NamedBlobImage(
        title=_(u'thumb'),
        required=False,
    )


@implementer(IProduct)
class Product(Item):
    """ Content-type class for IProduct
    """
