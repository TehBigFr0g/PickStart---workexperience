from xlwt import Workbook
import requests, bs4


wb = Workbook()
sheet1 = wb.add_sheet('Names')

athletes = open("names.txt","r")
teams = open("teams.txt","r")

count=0
sheet1.write(0,0,"NAMES")
sheet1.write(0,1,"TEAMS")

for x in athletes:
	sheet1.write(1+count,0,x)
	count = count+1

count=0

for x in teams:
	sheet1.write(1+count,1,x)
	count = count+1



wb.save('athletedirectory.xls')