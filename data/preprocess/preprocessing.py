# map the raw data into wiki_trusts.txt (src,tgt,sign) and wiki_comments.txt(src,tgt,comment)

import json
import re
import random

sample_ratio=0.4

with open('wiki-RfA.txt',"r") as f1,open('wiki_trusts_1000_sample.txt', 'w') as f3,open('training_set.txt', 'w') as f5,open('wiki_knows_1000_sample.txt', 'w') as f6:
	d = json.load(open("nameToUniqueidMap.txt"))
	src = ""
	tgt = ""
	vote = ""
	txt=""
	i=0
	
	total=0;
	pos=0;
	neg=0;

	visited=set()
	for line in f1:
		line = line.strip('\n')
		words = line.split(":")
		if len(words)<=1:
			continue

		if words[0]=="SRC":
			
		 	src=str(d[words[1].decode('utf-8')])
			# src=''
		if words[0]=="TGT":
			tgt=str(d[words[1].decode('utf-8')])
		if words[0]=="VOT":
			vote=words[1]
		if words[0]=="TXT":
			txt=words[1]

			matchObj = re.search(r'\'\'\'(.*)\'\'\'(.*)', txt, flags=0)  # remove "support/oppose" word in comments
			if matchObj:
				txt1=matchObj.group(2)
			else:
				txt1=txt

			if (src+':::'+tgt) not in visited:
				if vote!='0':    # remove neutral signs
					if int(src)<1000 and int(tgt)<1000:    # sample only 1000 users from all users 
						if vote=='1':
							if random.random()<sample_ratio:   # sample a certain rate of postive labels
								f3.write(src+'\t'+tgt+'\t'+'1'+'\n')
								f6.write(src+'\t'+tgt+'\t'+'1'+'\n')
								f5.write(src+':::'+tgt+':::'+vote+':::'+txt1+'\n')
								visited.add( src+':::'+tgt)
								pos=pos+1
						else:
							f3.write(src+'\t'+tgt+'\t'+'0'+'\n')	
							f6.write(src+'\t'+tgt+'\t'+'1'+'\n')
							f5.write(src+':::'+tgt+':::'+vote+':::'+txt1+'\n')
							visited.add( src+':::'+tgt)
							neg=neg+1
						
			src = ""
			tgt = ""
			vote = ""
			txt=""

		i=i+1
	total=pos+neg
	print "total:{}".format(total)
	print "positive label:{}".format(pos)
	print "negative label:{}".format(neg)
	print "N/P ratio:{}".format(neg/float(total))

	