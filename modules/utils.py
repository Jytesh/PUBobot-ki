#!/usr/bin/python2
# encoding: utf-8

def format_timestring(timelist):
	timeint = 0
	for i in timelist: #convert given time to float
		try:
			num=int(i[:-1]) #the number part
			if i[-1]=='d':
				timeint+=num*3600*24
			elif i[-1]=='h':
				timeint+=num*3600
			elif i[-1]=='m':
				timeint+=num*60
			elif i[-1]=='s':
				timeint+=num
			else:
				raise Exception("doh!")
		except:
			raise Exception("Bad argument @ \"{0}\", format is: 1h 2m 3s".format(i))
	return timeint

def split_large_message(text, delimiter="\n", charlimit=1999):
	templist = text.split(delimiter)
	tempstr = ""
	result = []
	print(templist)
	for i in range(0,len(templist)):
		tempstr += templist[i]
		msglen = len(tempstr)
		if msglen >= charlimit:
			raise("Text split failed!")
		elif i+1 < len(templist):
			tempstr += delimiter
			if msglen+len(templist[i+1]) >= charlimit-2:
				result.append(tempstr)
				tempstr = ""
		else:
			result.append(tempstr)
	return result

ranks = {
	5000: " 〈★〉",
	4500: "〈A+〉",
	4000: "〈A〉",
	3500: "〈B〉",
	3000: "〈C〉",
	2500: "〈D+〉",
	2000: "〈D-〉",
	1500: "〈E+〉",
	1000: "〈E〉",
	500: "〈E-〉",
	0: "〈F〉",
	-5000: "〈〉"}

def rating_to_icon(rating):
	for i in sorted(ranks.keys(), reverse=True):
		if rating >= i:
			return(ranks[i])
