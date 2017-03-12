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
For a Wikipedia editor to become an administrator, a request for adminship (RfA) must be submitted, either by the candidate or by another community member. Subsequently, any Wikipedia member may cast a supporting, neutral, or opposing vote. Besides, there is also a rich textual component in RfAs: each vote is typically accompanied by a short comment. (https://snap.stanford.edu/data/wiki-RfA.html).



