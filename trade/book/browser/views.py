#!/opt/plone/zinstance/bin/python2.7
# -*- coding: utf-8 -*-
import os
import sys
import base64
import time
import datetime
import transaction
from plone import api
from zope.interface import Interface
from z3c.relationfield import RelationValue
from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView
from plone.app.contentlisting.interfaces import IContentListing
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from OFS.interfaces import IOrderedContainer
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from plone.app.relationfield.behavior import IRelatedItems
from Products.CMFPlone.utils import base_hasattr
from urlparse import urlparse
from datetime import datetime
from datetime import date
from transaction import commit
from plone.uuid.interfaces import IUUID
# from uffs.site.browser.livroView import livroView

reload(sys)  
sys.setdefaultencoding('utf8')


class exemploView(BrowserView):
	index = ViewPageTemplateFile("templates/exemplo_view.pt")

	def __call__(self):
		return self.index()

	def getDate(self):
		dt = self.context.data.isoformat()
		dt = dt.split('-')
		yy = dt[0]
		mm = dt[1]
		dd = dt[2]

		return dd+'/'+mm+'/'+yy

class livroView(BrowserView):
	index = ViewPageTemplateFile("templates/livro_View.pt")

	def __call__(self):
		return self.index()

	def getDate(self, data):
		result = ''
		if data is not None:
			dt = data.isoformat()
			dt = dt.split('-')
			yy = dt[0]
			mm = dt[1]
			dd = dt[2]
			result = dd+'/'+mm+'/'+yy
		return result

	def getModificationDate(self):
		data_mod = self.context.ModificationDate(zone=None)
		data	 = data_mod.split('T',1)
		hora	 = data[1].split('-',1)[0].split(':')
		hora	 = hora[0]+'h'+hora[1]
		ts	     = time.strptime(data_mod[:19], "%Y-%m-%dT%H:%M:%S") 
		data	 = time.strftime("%d/%m/%Y", ts)
		return data+' às '+hora
