#reads all athletes names from excel doc
# saves names to names.txt

import xlrd

workbook = xlrd.open_workbook('athletedirectory.xls')
sheet = workbook.sheet_by_index(0)
num_rows = sheet.nrows - 1
curr_row = 0

#open up the file
names = open("names.txt","w")
instaFile = open("instagram.txt","w")
twitterFile = open("twitter.txt","w")

x=[]
# read all rows
for rownum in range(1,sheet.nrows):
	x.append(sheet.row_values(rownum))

# get all names
nms =[]
insta =[]
twitter =[]

count=0
for i in x:
	i=str(i)
	# read names from file
	nms.append(str(x[count][0])[0:(i.find('\n'))])
	# read instagram profile from file
	insta.append(str(x[count][3])[0:(i.find('\n'))])
	# read twitter profile from file
	twitter.append(str(x[count][6])[0:(i.find('\n'))])

	count = count+1

# write stuff to files
for i in nms:
	names.write(i+"\n")

for i in insta:
	instaFile.write(i+"\n")

for i in twitter:
	twitterFile.write(i+"\n")




