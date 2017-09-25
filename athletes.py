import requests, bs4

inFile = open("names.txt", "w")
teamsFile = open("teams.txt","w")

url = "http://www.pickstar.com.au/Athlete"

def get_word(bigword):
	first = bigword.find('>',1)
	last = bigword.find('<',first)
	return bigword[first+1:last]


def get_name(url):
	res=requests.get(url) 
	res.raise_for_status()
	soup=bs4.BeautifulSoup(res.text,"lxml")
	for link in soup.findAll('h4'):
		for y in link:
			y=str(y)
			if (y.find('small')!=-1):
				first_name = get_word(y)
			else:
				last_name = y
		inFile.write(first_name+" " +last_name + '\n')
	for link in soup.findAll('p'):
		for y in link:
			teamName=y
		teamsFile.write(str(teamName))

get_name(url)

inFile.close()