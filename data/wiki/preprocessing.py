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

		# if (words[0]=="SRC"):
		# 	src=words[1]
		# if (words[0]=="TGT"):
		# 	src=words[1]
		# if (words[0]=="SRC"):
		# 	src=words[1]
		# if (words[0]=="SRC"):
		# 	src=words[1]
		# if (words[0]=="TXT"):


	# for line in f:
	# 	line = line.strip('\n')
	# 	words = line.split(":")



		i=i+1
		if i<10:
			print line
			# print len(words)			
			print words[0]
			# print words[1]
	json.dump(d, open("map.txt",'w'))
# with open('map.txt',"w") as file1:


    