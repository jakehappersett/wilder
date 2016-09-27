#!/usr/bin/env python

import praw
from os import *
import urllib
from subprocess import call
r = praw.Reddit('gonewild top post bot')

files = os.listdir(os.curdir)
for f in files: 
	if f.endswith(jpg) or f.endswith(png):
		os.remove(f)

while True:
	sr = r.get_subreddit('gonewild')
	for submission in sr.get_top(limit=20):
		if submission.url[-4:] == '.jpg' or submission.url[-4:] == '.png' or submission.url[-4:] == '.gif':
			urllib.urlretrieve(submission.url, path.basename(submission.url))#path.basename('/gw'))
			#call(["feh --bg-scale %s" % path.basename(submission.url)])

			system("feh --bg-max %s" % path.basename(submission.url))
			break
	break
