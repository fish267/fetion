#!/usr/bin/python
#coding:utf-8
# fetion module 
# special thanks to http://quanapi.sinaapp.com/fetion.php

import urllib2
import sys
#------------------ initial fetion account------------------------------
sender = '15129245130'
passwd = 'a251125'
#receiver = '15129245130'
receiver = '15289084267'
#------------------ define fetion module--------------------------------
class Fetion:
	base_url = 'http://quanapi.sinaapp.com/fetion.php?'

	sender = ''
	passwd = ''
	receiver = ''
	def set_account(self, sender, passwd):
		self.sender = sender
		self.passwd = passwd
	def send_msg(self, receiver, msg):
		send_url = self.base_url + 'u=' + self.sender + '&p=' +\
			   self.passwd + '&to=' + receiver + '&m=' + msg
#		print send_url
		result = urllib2.urlopen(send_url).read()
		return eval(result)['result']
#-------------------send message via fetion-----------------------------
def main():
	fetion = Fetion()
	fetion.set_account(sender, passwd)
	while fetion.send_msg(receiver, sys.argv[1]) != 0:
		print 'Sending... Please wait'
	print 'Success!'
if __name__ == '__main__':
	main()
