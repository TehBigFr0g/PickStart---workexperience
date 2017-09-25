import requests,bs4

inFile = open("aflplayers.txt","w")
teamsFile = open("playersteams.txt","w")

def get_name(url):
	res=requests.get(url) 
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	for link in soup.findAll('strong'):
		link=str(link)
		x=link.find('itemprop="name"')
		if(x!=-1):
			start = link.find(">",x)
			end = link.find("<",start)
			inFile.write(link[start+1:end] + '\n')
	for link in soup.findAll('em'):
		for y in link:
			teamName=str(y)
		if(teamName.find('#')==-1 and teamName.find("Loading suggestions")==-1):
			teamsFile.write(teamName+'\n')


for x in range(1,89):
	get_name("http://www.aflplayers.com.au/playerpedia/all/page/"+str(x))