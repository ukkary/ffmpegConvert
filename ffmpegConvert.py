#!/usr/bin/python
#coding:utf-8

import os
import commands


def convert_video(url):
	try:
		directory = "/".join(url.split(".")[:-1][0].split("/")[:-1])
	except:
		directory = url.split(".")[:-1][0]
		
	callback = commands.getstatusoutput("sh ./convert.sh " + url + " " + directory)
	
 	if callback[0] == 0:
 		notify(1, url)
	else:
		notify(2, url)

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
	
def notify(x, src):
	base = "terminal-notifier -title 'ffmpegConverter' -message '"
	
	if x == 1:
		commands.getoutput(base + src + "  が変換されました'")	
	if x == 2:
		commands.getoutput(base + src + "  の変換に失敗しました'")
	if x == 3:
		commands.getoutput(base + "  変換が終わりました'")	
	if x == 4:
		commands.getoutput(base + "   変換できるものがありません")
		
if __name__ == "__main__":
	_in = get_path("input")
	_out = get_path("output")

	for i in range(len(_in)):
		if _in[i] not in _out:
			convert_video(_in[i])

	#notify(3, "null")