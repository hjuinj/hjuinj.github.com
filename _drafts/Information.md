---
title: "Information Theory"
author: "hjuinj"
date: "27 October 2015"
output: html_document
---

#Source Coding
As it is desirable to transmit as few bits as possible, it is good to try to compress the amount of information requried to be sent.

After which additional sequence of bits are added to reduce the bit error (channel encoding) caused by the channel

##Lossless coding
Ensures all of the original information is kept through the encoding.
###Informational Entropy 
Average (weighted sum) informationi content within a bit, taking into account the likelihood of a bit turning out to be 1 or 0. 
The maximum level of information is obtained when it is equally likely to retrive a 1 or 0 from the unknown bit.

Summarising to the case where more than two possiblities(rather than only 1 or 0) can arise,
the general expression goes as: 
$$H = -\sum_{i=1}^k p_i log(p_i)$$
where i denotes one out of k possible outcomes of a random variable. The k possible outcomes is basically the fundamental unit of the message we try to convey, i.e. it can the alphabet (plus a few punctuations) of the English language.

###Huffman compression 
When the possible outcomes are not uniformly distributed, H would reduce. This is a measure of the lower bound of the **average** code length needed. 
Lower the H, the less encoding. Huffman compression exploit this by recursively combining the least frequent two outcomes together to creat a new parent node until all outcomes have combined into a (unbalanced) binary tree. 
(CS101 from Harvard has a fairly good Huffman tree decoding programming exercise in C, try write the Huffman encoding as well if you are interested)
To ensure unique representation of these outcomes using only 1 and 0, 1 is usually chosen as the stopping bit, so the most likely/frequently visited node is represented by 1, and the next 01, the next 001 ... the second last 0....01 and the final node 0....00.

The performance of this encoding is not necessary the most optimal, though .


Given the probability of each outcome as an array, here is a quick hack of the steps it takes to merge it into a tree in python.

```python
def tree(probArray):
      #threshold of 10**-3 could change depending on how sensitive the inital probabilities are
	while abs(sum(probArray) - len(probArray)) > 10**-3: 
		a = probArray.index(min(probArray))
		temp = probArray[probArray.index(min(probArray))]
		probArray[probArray.index(min(probArray))] = 1
		b = probArray.index(min(probArray))
		print("merge " + str(a) + " and " + str(b))
		probArray[probArray.index(min(probArray))] += temp
```