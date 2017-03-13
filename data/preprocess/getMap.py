#  get the map function file from SRC/TGT name to unique id
import json
with open('wiki-RfA.txt',"r") as f1 :
	i=0
	count=0
	d=dict()

	for line in f1:
		line = line.strip('\n')
		words = line.split(":")
		if len(words)<=1:
			continue

		if (words[0]=="SRC" or words[0]=="TGT"):

			if words[1] not in d:
				count=count+1
				d[words[1]]=count

	json.dump(d, open("nameToUniqueidMap.txt",'w'))
	print "number of unique user: "+str(count)


    