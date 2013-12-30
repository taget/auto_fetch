#!/usr/bin/env python
#encoding=utf-8
import re
from config import config
import util

class patch():
	
	def __init__(self, message):
		self._message = message
		self._body = ''
		self._valid = False
		self._build = ''
		self._name = ''
		self._from = ''
		self._date = ''
		
		self.pass_message()
	
	def get_body(self):
		return self._body
		
	def get_git_name(self):
		return self._name;
		
	def get_branch(self):
		return self._branch
	
	def is_valid(self):
		return self._valid
	
	def get_subject(self):
		return self._message_subject
		
	def pass_message(self):
		self._message_subject = util.trim(self._message['subject'])
		self._from = self._message['From']
		self._date = self._message['Date']
		self._body = self._message.get_payload(decode=True)
		try:
			(self._build, self._name) = \
			      util.get_branch_gitname(self._message_subject)
		except:
			self._valid = False
		else:
			self._valid = True
	
	
	def test(self):
		print "self._message_subject %s" % self._message_subject
		a = 'ok' if self._valid == True else 'false'
		print a
		
if __name__ == "__main__":
	pass
