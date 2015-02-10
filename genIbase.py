# This should get data for Gen I Base Stats

# Import stuff
# This is for handling urls
import requests
# This is for web parsing
from bs4 import BeautifulSoup
# This is for writing to a csv
import csv

# Open file and csv.
# The 'wb' makes sure there is not an extra line,
# unlike just 'w', happens because of Windows.
# Make sure to have the file closed, if already ran and opened
f = open('C:/PandP/GenIBaseStats/GenIBaseStats.csv','wb')
writer = csv.writer(f)

# Write the header for the file
writer.writerow(['Number', 'Name', 'HP', 'Attack', 'Defense', 'Speed', 'Special'])

# Get the url and webpage
# Yeah, it's a mess
url = ("http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon"
	   "_by_base_stats_%28Generation_I%29#List_of_Pok.C3.A9mon_by_base_stats")
page = requests.get(url)
soup = BeautifulSoup(page.text)

# To see the actual page,
# print(soup)

# Use the Firebug add-on to find out where the table is on screen.
# getfirebug.com
# Open it up at the bottom of the screen
# Move your cursor on the code to highlight the webpage
# Find in the code what you need to find

# style="background:#FFFFFF" will get the rows of the big table
# Not a general rule for all tables
# Just works because its the set color for this one table
rows=soup.find_all(style="background:#FFFFFF")

# Loop through the rows to get the data and write it out
for r in rows:
	#             0     1       2   3    4   5   6  7   8 
	# contents = ['',dex number,'',image,'',name,'',HP,'',Attack...]
	conts = r.contents
	# Get the number first
	Number = conts[1].contents[1].get_text()
	# Check if it's a Nidoran
	# The male/female signs throw everything off
	if Number not in ['029','032']:
		Name = conts[5].contents[1].get_text()
		HP = conts[7].get_text()[:-1]
		Attack = conts[9].get_text()[:-1]
		Defense = conts[11].get_text()[:-1]
		Speed = conts[13].get_text()[:-1]
		Special = conts[15].get_text()[:-1]
		#print([Number, Name, HP, Attack, Defense, Speed, Special])
		writer.writerow([Number, Name, HP, Attack, Defense, Speed, Special])
	# if Nidoran female
	elif Number == '029':
		Name = 'Nidoran_F'
		HP = conts[7].get_text()[:-1]
		Attack = conts[9].get_text()[:-1]
		Defense = conts[9].get_text()[:-1]
		Speed = conts[9].get_text()[:-1]
		Special = conts[9].get_text()[:-1]
		#print([Number, Name, HP, Attack, Defense, Speed, Special])
		writer.writerow([Number, Name, HP, Attack, Defense, Speed, Special])
	# if Nidoran male
	elif Number == '032':
		Name = 'Nidoran_M'
		HP = conts[7].get_text()[:-1]
		Attack = conts[9].get_text()[:-1]
		Defense = conts[9].get_text()[:-1]
		Speed = conts[9].get_text()[:-1]
		Special = conts[9].get_text()[:-1]
		#print([Number, Name, HP, Attack, Defense, Speed, Special])
		writer.writerow([Number, Name, HP, Attack, Defense, Speed, Special])
	# If something goes wrong
	else:
		print 'ERROR'

# Close file
f.close()

# Show finished
print 'Done'
