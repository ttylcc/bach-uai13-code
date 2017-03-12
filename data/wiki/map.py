# map the raw data into wiki_trusts.txt (src,tgt,sign) and wiki_comments.txt(src,tgt,comment)

import json
import re
with open('wiki-RfA.txt',"r") as f1,open('hash_wiki.txt', 'w') as f2,open('wiki_trusts.txt', 'w') as f3,open('wiki_comments.txt', 'w') as f4,open('training_set.txt', 'w') as f5:
	d = json.load(open("map.txt"))
	src = ""
	tgt = ""
	vote = ""
	txt=""
	i=0
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
			# tgt=''
		if words[0]=="VOT":
			vote=words[1]
		if words[0]=="TXT":
			txt=words[1]
			matchObj = re.search(r'\'\'\'(.*)\'\'\'(.*)', txt, flags=0)
			
			if matchObj:
				txt1=matchObj.group(2)
				# print txt1
				# txt1='1'
			else:
				txt1=txt
			if (src+':::'+tgt) not in visited:
				if vote!='0':
					f2.write(src+':::'+tgt+':::'+vote+':::'+txt+'\n')
					f3.write(src+':::'+tgt+':::'+vote+'\n')
					f4.write(src+':::'+tgt+':::'+txt1+'\n')
					f5.write(vote+':::'+txt1+'\n')
					visited.add( src+':::'+tgt);


			
			src = ""
			tgt = ""
			vote = ""
			txt=""

		i=i+1
	