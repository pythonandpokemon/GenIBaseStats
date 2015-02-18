# imports
import matplotlib.pyplot as plt;
import pandas
import numpy
import seaborn as sns

# Read in the data
BaseStats = pandas.read_csv("C:\PandP\GenIBaseStats\GenIBaseStats.csv")
Types = pandas.read_csv("C:\PandP\GenITypes\GenITypes.csv")
# Combine the data together so that each Pokemon's types are represented
# If a Pokemon has two types, it is listed twice
# Just stack the sets
Data = pandas.merge(BaseStats,Types.drop('Name',axis=1),on="Number")
Type1 = Data.drop("Type2",axis=1)
Type1.rename(columns={"Type1":"Type"}, inplace = True)
Type2 = Data.drop("Type1",axis=1)
Type2.rename(columns={"Type2":"Type"}, inplace = True)
Type2 = Type2[pandas.notnull(Type2['Type'])]
Data = Type1.append(Type2)

# Save the list of types
types = []
# Restructure the data
HPbyType = numpy.empty(len(Data['Type'].unique()), dtype=pandas.Series)
for i, type in enumerate(sorted(Data['Type'].unique())):
	types.append(type)
	HPbyType[i]=pandas.Series(Data['HP'][Data['Type']==type],name=str(type))

# Max value so that all the plots are on the same scale
maxVal = Data.ix[:,2:7].max().max()

# Make the plot
# and add plot features
print("HP")
sns.boxplot(vals=HPbyType)
plt.ylim((0,maxVal))
ind = numpy.arange(1,len(Data['Type'].unique())+1)
plt.xticks(ind, types)
plt.xticks(rotation=70)
plt.xlabel('Types')
plt.ylabel('Mean HP')
plt.title('HP by Type')
plt.tight_layout()
# This line has to come before plt.show()
plt.savefig("C:\PandP\GenIBaseStats\BaseGraphs\HP.pdf")
plt.show()

# Rerun through the other stats
for stat in Data.columns[3:7]:
	print(stat)
	plt.clf()
	
	StatbyType = numpy.empty(len(Data['Type'].unique()), dtype=pandas.Series)
	for i, type in enumerate(sorted(Data['Type'].unique())):
		types.append(type)
		StatbyType[i]=pandas.Series(Data[stat][Data['Type']==type],name=str(type))

	sns.boxplot(vals=StatbyType)
	plt.ylim((0,maxVal))
	plt.xticks(ind, types)
	plt.xticks(rotation=70)
	plt.xlabel('Types')
	plt.ylabel('Mean ' + stat)
	plt.title(stat + ' by Type')
	plt.tight_layout()
	# This line has to come before plt.show()
	plt.savefig("C:\PandP\GenIBaseStats\BaseGraphs\\" + stat + ".pdf")
	plt.show()

