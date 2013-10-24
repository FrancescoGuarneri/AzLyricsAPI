#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       AZLyricsAPI.py, mini-API for AZLyrics
#
#       Copyright 2013 Francesco Guarneri <Black_Ram>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from lxml import etree
import urllib2
import StringIO

def generating(artist, title, save):
		artist = ''.join(artist.split())
		title = ''.join(title.split())
		generate_url = 'http://azlyrics.com/lyrics/'+artist+'/'+title +'.html'
		processing(generate_url, artist, title, save)
		
def processing(generate_url, artist, title, save):
	response = urllib2.urlopen(generate_url)
	read_lyrics = response.read()
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO.StringIO(read_lyrics), parser)
	lyrics = tree.xpath("//div[@style='margin-left:10px;margin-right:10px;']/text()")
	printing(artist, title, save, lyrics)
	
def printing(artist, title, save, lyrics):
	for words in lyrics:
		print str(words).strip()
	
	if save == True:
		saving(artist, title, lyrics)
	elif save == False:
		pass
			
def saving(artist, title, lyrics):
		f = open(artist + '_' + title + '.txt', 'w')
		f.write("\n".join(lyrics).strip())
		f.close()
