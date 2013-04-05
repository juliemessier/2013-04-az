import sys 
import screed
filename = sys.argv[1]
print filename
count = 0
for record in screed.open(filename):

	print record["sequence"]
	if count>20:
		break
	count +=1
