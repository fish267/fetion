# coding:utf-8
# get information from http://tianqi.cncn.com/lhasa
# return weather information and suggestions about travel or sports
# author: fish 

import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://tianqi.cncn.com/lhasa'
def weather_information(location_url):
	soup = BeautifulSoup(urllib2.urlopen(location_url).read())
	weather = soup.find('div', 'tianqi').ul.li.find_all('strong')
	suggestion = soup.find('div', 'txt').find_all('p')
	return    str(weather[1])[8:-9] + ',' +  str(weather[2])[8:-9] + \
		'^_^*^_^'+ 	'穿衣提醒:' + str(suggestion[1])[25:-7] + ';' + \
		'游玩:' + str(suggestion[0])[25:-7] 
