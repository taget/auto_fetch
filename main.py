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
import logging
import os

class autofetch:
	def __init__(self):
		
		self._conf = config()
		self._user = self._conf.get('user')
		self._password = self._conf.get('password')
		self._git_list = self._conf.get('git').split(',')
		self._logger_file = self._conf.get('log')
		
		# set log file
		self._logger = logging.getLogger()
		hdlr = logging.FileHandler(self._logger_file)
		formatter = logging.Formatter('%(asctime)s \
		                     %(levelname)s %(message)s')
		hdlr.setFormatter(formatter)
		self._logger.addHandler(hdlr)
		self._logger.setLevel(logging.NOTSET)
		
		# mail object
		self._mailobj = mail(self._conf)
		# mail object

	def info(self, msg):
		self._logger.info(msg)

	def error(self, msg):
		self._logger.error(msg)
	
	def test(self):
		print self._git_list

	def persist(self, obj):
		'''
		persist obj to a file
		'''
		dirname =  obj.get_git_name()
		filename = obj.get_subject()
		if not os.path.exists(dirname):
			os.mkdir(dirname)
		file_name = dirname + '/' + filename
		self.info("ready to persist:" + file_name)
		try:
			f = open(file_name, 'w')
			print obj.get_body()
			f.write(obj.get_body())
			self.info("persist ok : " + file_name)
		except:
			self.error("persist error : " + file_name)
			pass

	def persist_all(self, objs):
		for obj in objs:
			if obj.is_valid():
				self.persist(obj)
	
	def start(self):
		objs = self._mailobj.get_mailobjs('^\[Frobisher\]')
		for obj in objs:
			if obj.is_valid() and obj.get_git_name() in \
			                    self._git_list:
				self.info(obj.get_git_name())
				
		self.persist_all(objs)
		
# create a summary log
# how many patch
# which is valid
	def summary(self):
		pass
		
def main():
	
	af = autofetch()
	af.start()

if __name__ == '__main__':
	main()

