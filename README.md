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

Wikipedia Requests for Adminship (with text)
--------
For a Wikipedia editor to become an administrator, a request for adminship (RfA) must be submitted, either by the candidate or by another community member. Subsequently, any Wikipedia member may cast a supporting, neutral, or opposing vote. This induces a directed, signed network in which nodes represent Wikipedia members and edges represent votes. In this sense, the present dataset is a more recent version of the Wikipedia adminship election data. However, there is also a rich textual component in RfAs, which was not included in the older version: each vote is typically accompanied by a short comment (median/mean: 19/34 tokens). A typical positive comment reads, "I've no concerns, will make an excellent addition to the admin corps", while an example of a negative comment is, "Little evidence of collaboration with other editors and limited content creation."
(https://snap.stanford.edu/data/wiki-RfA.html).



