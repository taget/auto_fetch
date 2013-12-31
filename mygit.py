#!/usr/bin/env python
#encoding=utf-8

from git import *
import git

class mygit:
	def __init__(self, repo_dir, git_url):
		self._repo_dir = repo_dir
		self._git_url = git_url
		Repo.clone_from(self._git_url, \
		                              self._repo_dir)
		try:
			self._repo = Repo(self._repo_dir)
		except:
			print "my git init error!"
			pass
		
	def checkout(self, branch):
		g = self._repo.git
		g.checkout(branch)
		if not self._repo.head.reference == branch:
			return False
		else:
			return True
			
	def am(self, patch_file):
		g = self._repo.git
		try:
			g.am(patch_file)
		except:
			# todo g.am('abort') --abort
			g.am('abort')
			return False
		else:
			return True

# Give a patch list to am
	def am_batch(self, patch_list):
		for patch in patch_list:
			if False == self.am(patch):
				return False
	
		
if __name__ == "__main__":
	pass

