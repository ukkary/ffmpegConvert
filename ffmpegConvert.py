#!/usr/bin/python
#coding:utf-8

import os
import commands


def convert(url):
	try:
		source = "/".join(url.split(".")[:-1][0].split("/")[:-1])
	except:
		source = url.split(".")[:-1][0]
		
	callback = commands.getstatusoutput("sh ./convert.sh " + url + " " + source)
	
 	if callback[0] == 0:
 		alert(1, url)
	else:
		alert(2, url)

def get_path(base_path):
	dir_list = []
	sub_dir = []

	for root, dir, files in os.walk(base_path):
		for name in files:
			sub_dir.append(os.path.join(root, name))	
				
  	for d in sub_dir:
  		if d.split(".")[-1] == "mp4":
  			dir_list.append("/".join(d.split("/")[1:]))

 	return dir_list
	
def alert(x, name):
	base = "terminal-notifier -title 'ffmpegConverter' -message '"
	
	if x == 1:
		commands.getoutput(base + name + "  が変換されました'")	
	if x == 2:
		commands.getoutput(base + name + "  の変換に失敗しました'")
	if x == 3:
		commands.getoutput(base + "  変換が終わりました'")	
	if x == 4:
		commands.getoutput(base + "   変換できるものがありません")
		
if __name__ == "__main__":
	inp = get_path("input")
	out = get_path("output")

	for i in range(len(inp)):
		if inp[i] not in out:
			convert(inp[i])

	#alert(3, "null")