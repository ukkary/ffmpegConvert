#!/usr/bin/python
#coding:utf-8


import os
import sys
import os.path
import commands


try_flag = False
count = 0

def convert(url):
	try:
		ss = url.split(".")[:-1][0].split("/")[:-1]
		source = "/".join(ss)
	except:
		source = url.split(".")[:-1][0]
		
	callback = commands.getstatusoutput("sh ./convert.sh " + url + " " + source)
	alert(1, url)
 	if callback[0] == 0:
		return True
	else:
		alert(3, "e")
	
def get_path(num):
	lis = []
	subdir = []

	if num == 0:
		for root, dir, files in os.walk("input"):
			for name in files:
				subdir.append(os.path.join(root, name))
				
	elif num == 1:
		for root, dir, files in os.walk("output"):
			for name in files:
				subdir.append(os.path.join(root, name))
	
  	for dir in subdir:
  		if dir.split(".")[-1] == "mp4":
  			s = dir.split("/")[1:]
  			lis.append("/".join(s))

 	return lis
	
def alert(x, name):
	if x == 1:
		base_b = "terminal-notifier -title 'ffmpegConverter' -message '"
		base_e = "  が変換されました'"
		commands.getoutput(base_b + name + base_e)
		
	if x == 2:
		base_b = "terminal-notifier -title 'ffmpegConverter' -message '変換するものがありません'"
		
	if x == 3:
		base_b = "terminal-notifier -title 'ffmpegConverter' -message '変換に失敗しました'"
		
if __name__ == "__main__":
	input = get_path(0)
	output = get_path(1)
	
 	while True:
 		output.append("e")
 		if len(input) < len(output):
 			break

	for i in range(len(input)):
		if input[i] not in output:
			convert(input[i])
		else:
			alert(2, "e")