CS249 Project
===============

This is the CS249 course project, and the repository is forked from (https://github.com/stephenbach/bach-uai13-code), which is the code for "Hinge-loss Markov Random Fields: Convex Inference for Structured Prediction." Stephen H. Bach, Bert Huang, Ben London, and Lise Getoor. Uncertainty in Artificial Intelligence (UAI) 2013. 

Instructions
=============

Prerequisites
-------------
This software depends on Java 6/7 and Maven 3 (http://maven.apache.org). Matlab and
Python (>=2.7) are also required to process the results.

PSL Library
-----------
The algorithms for these experiments are implemented in the PSL library, version 1.1
(https://github.com/linqs/psl/tree/1.1). It will be downloaded by Maven automatically.

Executing
---------
Each experiment can be run from one of the shell scripts in the root directory.

Data
====

Epinions
--------
This data set is a snowball sample from the Epinions trust data set
(http://snap.stanford.edu/data/soc-sign-epinions.html).

From the website:
"This is who-trust-whom online social network of a a general consumer review site Epinions.com.
Members of the site can decide whether to ''trust'' each other. All the trust relationships
interact and form the Web of Trust which is then combined with review ratings to determine
which reviews are shown to the user."

Please cite the original data set as

	@inproceedings{leskovec:chi10,
		author = "Leskovec, Jure and Huttenlocher, Daniel and Kleinberg, Jon},
		booktitle = "{28th ACM Conference on Human Factors in Computing Systems (CHI)}",
		pages = "1361--1370",
		title = "Signed Networks in Social Media",
		year = "2010"
	}


