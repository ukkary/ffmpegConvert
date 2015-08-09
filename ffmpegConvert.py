#!/usr/bin/python
#coding:utf-8

import os
import sys
import commands


try_flag = False

def convert(url):
	try:
		ss = url.split(".")[:-1][0].split("/")[:-1]
		source = "/".join(ss)
	except:
		source = url.split(".")[:-1][0]
	callback = commands.getstatusoutput("sh ./convert.sh " + url + " " + source)
 	if callback[0] == 0:
 		alert(1, url)
		return True
	else:
		alert(3, "e")
		return False
	
def get_path(path):
	lis = []
	subdir = []

	for root, dir, files in os.walk(path):
		for name in files:
			subdir.append(os.path.join(root, name))
				
  	for d in subdir:
  		if d.split(".")[-1] == "mp4":
  			s = dir.split("/")[1:]
  			lis.append("/".join(s))
 	return lis
	
def alert(x, name):
	base = "terminal-notifier -title 'ffmpegConverter' -message '"
	
	if x == 1:
		commands.getoutput(base + name + "  が変換されました'")
	if x == 2:
		commands.getoutput(base + "   変換が終わりました'")	
	if x == 3:
		commands.getoutput(base + "   変換に失敗しました'")
		
if __name__ == "__main__":
	inp = get_path("input")
	out = get_path("output")
	argv = sys.argv
	
 	while True:
 		out.append("e")
 		if len(inp) < len(out):
 			break

	for i in range(len(inp)):
		if inp[i] not in out:
			convert(inp[i])
		else:
			alert(2, "e")