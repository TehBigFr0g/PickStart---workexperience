#get twitter data for given name
import requests,bs4
from google import search


def getCount(url):
	if(url==-1):
		return -1
	if(url.find("twitter.com")==-1):
		return -1
	if(url.find("status")!=-1): # make sure its not a photo, we need the user page
		return -1
	if(url.find("hasn't Tweeted")!=-1):
		return -1
	res=requests.get(url) 
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	soup=str(soup)
	section=soup.find('ProfileNav-item--followers')
	find = soup.find('data-count',section) # find count from soup
	start = soup.find('"',find)
	end = soup.find('"',start+1)
	count = soup[start+1:end]
	try:
		count = int(count)
		if (int(count) <1000): # user not very popular -> unlikely to be sport related
			return -1
	except ValueError:
		print('ERROR')
		return -1

	return count

def getUsername(url): # returns insta username
	if(url.find("twitter.com")==-1):
		return -1
	if(url.find("/p/")!=-1):
		return -1
	base = url.find(".com")
	start = url.find("/",base)
	end = url.find("?",start+1)
	return url[start+1:end]

def getAddress(text):
    for url in search(text,stop=1,pause=3.0): # google search, take first url
    	if(url.find("status")!=-1):
    		return -1
    	if(url.find("twitter.com")!=-1): # check to make sure url has instagram in it
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
	address=getAddress(x+" twitter") # search for name + instagram
	address=str(address)
	print(address)
	w_sheet.write(count,5,address)
	username=getUsername(address)
	username=str(username)
	print(username)
	w_sheet.write(count,6,username)
	followers = getCount(address)
	followers=int(followers)
	print(followers)
	w_sheet.write(count,7,followers)
	print("Completed "+str(count) +" athletes")
	count=count+1
	wb.save('athletedirectory.xls')



wb.save('athletedirectory.xls')
