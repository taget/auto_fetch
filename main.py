#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 qiaoliyong <qiaoliyong@localhost.localdomain>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from config import config
from mail import mail
from mygit import mygit
import log
import os
import shutil


class autofetch:
	def __init__(self):
		
		self._conf = config()
		self._git_list = self._conf.get('git').split(',')
		self._logger = log.getLogger(self.__module__)
		self._patchdir = self._conf.get('patchdir')
		self._git_dir = self._conf.get('gitdir')
		# mail object
		self._mailobj = mail(self._conf)

	@property
	def logger(self):
		"logger is a property not a function"
		return self._logger
	
	def persist(self, obj):
		'''
		persist obj to a file
		'''
		dirname =  self._patchdir + '/' + obj.get_git_name()
		filename = obj.get_subject()
		if not os.path.exists(dirname):
			os.mkdir(dirname)
		file_name = dirname + '/' + filename
		self.logger.debug("ready to persist [%s]" % file_name)
		try:
			f = open(file_name, 'w')
			f.write(obj.get_body())
			obj.set_path(file_name)
			self.logger.info("persist [%s] ok ! " % file_name)
		except:
			self.logger.error("persist [%s] error !" % file_name)
			pass

	def persist_all(self, objs):
		if os.path.exists(self._patchdir):
			shutil.rmtree(self._patchdir)
		os.mkdir(self._patchdir)
		for obj in objs:
			if obj.is_valid():
				self.persist(obj)
	
	# create a summary log
	# how many patch
	# which is valid
	def summary(self, obj):
		self.logger.debug("Valid: [%s]" % 'yes' \
		             if obj.is_valid() else 'No')
		self.logger.debug("Subject: [%s]" % obj.get_subject())
		self.logger.debug("Sender: [%s]" % obj.get_sender())
		self.logger.debug("Date: [%s]" % obj.get_date())


	def clean_dir(self, base, l):
		for s in l:
			path = base + '/' + s
			if os.path.exists(path):
				shutil.rmtree(path)

	def process_git(self):
		pass
		

	def start(self):
		
		# clean up
		self.clean_dir(self._patchdir, self._git_list)
		self.clean_dir(self._git_dir, self._git_list)
		# get mail objs
		objs = self._mailobj.get_mailobjs('^\[Frobisher\]')
		for obj in objs:
			if obj.get_git_name() in self._git_list:
				self.summary(obj)

		self.persist_all(objs)
		print "get [%d] patch obj(s)" % len(objs)



				
def main():
	
	af = autofetch()
	af.start()

if __name__ == '__main__':
	main()

