---
title: "NLP"
author: "hjuinj"
date: "29 November 2015"
output: html_document
---
1. Contents
{:toc}
#Overview:
To summarize, the knowledge of language needed to engage in com-
plex language behavior can be separated into six distinct categories.
- Phonetics and Phonology – The study of linguistic sounds.
- Morphology – The study of the meaningful components of words.
- Syntax – The study of the structural relationships between words.
- Semantics – The study of meaning.
- Pragmatics – The study of how language is used to accomplish goals.
- Discourse – The study of linguistic units larger than a single utterance.

#Language Model
## Trigram Model
A language model where the occurence of a word in the sentence depends on the occurence of
the two words that appear previous to it. 
In "A big cat", the trigram estimate is 
q(cat | A, big) = Count(A, big, cat)/Count(A, big)

the count of such sequence of words is obtained from a training set of sentences. Likewise
bigram, unigram, quartgram....etc models can be defined

### Linear interpolation
Using different level of estimate, i.e. trigram, bigram and unigram estimates, the model
perform differntl depending on training size. This is a classical bias-variance tradeoff,
where the trigram estimate would converge to the best model with increasing amount of data
because presumebly more contexts would be convered with this. But with moderate amount of
data most of the word combination would not appear making such particular estimate zero.
The reverse arguement apply to unigram estimate.

Linear interpolation threads together these three (or estimates up to any degree)
estimations by summing their weighted sum. The weights are estiamted using a validation set.

### Discounting method
Another estimation method.Instead of setting unseen words/word conbinations a probability
of zero. This method takes away 0.5 from the total counts of each word combination, 
therefore making the total probaility 'p' smaller than zero. The remainder probability
1-p is then assagined to any unseen word combinations in accordance to the frequency of each
word appearing in the dataset.


#Tagging
Supervised learning problem, using tagged corpus to tagg each word within a sentence that
is indicative of a desired property
##Conditional model
p(y|x)

##Generative model
p(x,y) in terms of p(y)p(x|y)
then p(x,y) can be turned into p(y|x) when needed through Bayes Rule by dividing by p(x)

But in the 