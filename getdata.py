import requests,bs4
from google import search


def getInstaCount(url):
	if(url==-1):
		return -1
	if(url.find("instagram.com")==-1):
		return -1
	if(url.find("/p/")!=-1): # make sure its not a photo, we need the user page
		return -1
	res=requests.get(url) 
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	soup=str(soup)
	find = soup.find('{"count":') # find count from soup
	start = soup.find(":",find)
	end = soup.find("}",start)
	count = soup[start+2:end]
	if (int(count) <1000): # user not very popular -> unlikely to be sport related
		return -1
	return count

def getInstaUsername(url): # returns insta username
	if(url.find("instagram.com")==-1):
		return -1
	if(url.find("/p/")!=-1):
		return -1
	base = url.find(".com")
	start = url.find("/",base)
	end = url.find("/",start+1)
	return url[start+1:end]

def getInstaAddress(text):
    for url in search(text,stop=1,pause=2.0): # google search, take first url
    	if(url.find("instagram.com")!=-1): # check to make sure url has instagram in it
    		r = requests.get(url)
    		if(r.status_code==404): # if url is bad
    			return -1
    		return url
    	
    return -1

from xlwt import *
from xlutils.copy import copy
from xlrd import open_workbook

rb = open_workbook('athletedirectory.xls',formatting_info=True)
r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy


athletes = open("names.txt","r").readlines()
instaFile = open("insta.txt","w")
count=1


for x in athletes:
	address=getInstaAddress(x+" instagram") # search for name + instagram
	address=str(address)
	print(address)
	w_sheet.write(count,2,address)
	instaFile.write(address+" ")
	username=getInstaUsername(address)
	username=str(username)
	print(username)
	w_sheet.write(count,3,username)
	instaFile.write(username+" ")
	followers = getInstaCount(address)
	followers=int(followers)
	print(followers)
	w_sheet.write(count,4,followers)
	instaFile.write(str(followers)+"\n")
	print("Completed "+str(count) +" athletes")
	count=count+1
	wb.save('athletedirectory.xls')



wb.save('athletedirectory.xls')

