#!/usr/bin/python
#coding:utf-8

import os
import commands


def convert(url):
	try:
		s = url.split(".")[:-1][0].split("/")[:-1]
		source = "/".join(s)
	except:
		source = url.split(".")[:-1][0]
		
	callback = commands.getstatusoutput("sh ./convert.sh " + url + " " + source)
	
 	if callback[0] == 0:
 		alert(1, url)
		return True
	else:
		alert(3, "e")
		return False
	
def get_path(base_path):
	dir_list = []
	sub_dir = []

	for root, dir, files in os.walk(base_path):
		for name in files:
			sub_dir.append(os.path.join(root, name))	
				
  	for d in sub_dir:
  		if d.split(".")[-1] == "mp4":
  			s = d.split("/")[1:]
  			dir_list.append("/".join(s))

 	return dir_list
	
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
	
 	while True:
 		out.append("null")
 		if len(inp) < len(out):
 			break

	for i in range(len(inp)):
		if inp[i] not in out:
			convert(inp[i])
	
	alert(2, "e")