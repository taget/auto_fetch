#!/usr/bin/env python
#encoding=utf-8
import re
import sys
import time
import email
import imaplib


from config import config
from patch import patch

class mail():
	
	def __init__(self, conf):
		self._user = conf.get('user')
		self._password = conf.get('password')
		self._maildir = conf.get('maildir')
		self._mailserver = conf.get('mailserver')
		self._port = 993
		
	def get_mailobj(self, subject):
		'''
		get mail obj
		'''
		mailobjs = []
		
		p = imaplib.IMAP4_SSL(self._mailserver, self._port)
		p.login(self._user, self._password)
		
		p.select(self._maildir)	
		
		# Read Unseen mail
		# Marked as seen
		# Find $subject and mark Flagged
		mailresp, mailitmes = p.search(None, "UNSEEN")
		for num in mailitmes[0].split():
			typ, data = p.fetch(num, '(BODY.PEEK[])')
			
			mailText = data[0][1]
			mail_message = \
			              email.message_from_string(mailText)
			# find subject
			if re.search(subject, mail_message['subject']):
				try:
					obj = patch(mail_message)
					mailobjs.append(obj)
				except:
					raise
				else:
				# Mark Flagged
					p.store(num, '+FLAGS','\\Flagged')
			#p.store(num, '+FLAGS','\\Seen')
			
		p.close()
		p.logout()
		return mailobjs


if __name__ == "__main__":
	# 
	c = config()
	m = mail(c)
	objs = m.get_mailobj('^\[Frobisher\]')
	
	for obj in objs:
		print obj
		print obj.get_git_name()
		obj.test()
