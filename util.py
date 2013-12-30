#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  util.py
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


import string

def get_branch_gitname(sb):
	try:
		tmp = sb.split('] [')[1].split(' ')
	except:
		raise
	return (tmp[0], tmp[2])
	
def trim(sb):
	r = sb
	r = string.replace(r, '\\' , '_')
	r = string.replace(r, '/' , '_')
	return r
	
if __name__ == "__main__":
	sb = '[Frobisher] [build7 PATCH qemu v3 04/14] core: add more cow-bell'
	(a, b) = get_branch_gitname(sb)
	print a
	print b
	print trim(sb)
