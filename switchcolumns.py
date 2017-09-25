#file to seperate team and sport type from teams.txt

teams = open("teams.txt","r").readlines()

from xlwt import *
from xlutils.copy import copy
from xlrd import open_workbook

rb = open_workbook('athletedirectory.xls',formatting_info=True)
r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
wb = copy(rb) # a writable copy (I can't read values out of this, only write to it)
w_sheet = wb.get_sheet(0) # the sheet to write to within the writable copy


i=0
#for second and third rows
for row in teams:
	#w_sheet.write(row,col,text)
	first = row.find("-")
	playerTeam = row[0:first-1]
	w_sheet.write(i+1,1,playerTeam)
	playerSport = row[first+2:len(teams[i])]
	w_sheet.write(i+1,2,playerSport)
	i=i+1

wb.save('athletedirectory.xls')