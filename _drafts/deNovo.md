---
title: "de Novo Drug Design"
layout: post
author: "hjuinj"
date: "23 October 2015"
output: html_document
---

On 23/10/2015 Prof. Dr. Gesibert Schneider paied UCB a visited after his lecture circuit around Southern England and presented researches that's been carried out in his group at ETH in recent years. 
It is a beautiful combination of life sciences and computer sciences in the form of *de novo* drug design, involving medicinal chemistry, molecular biology, machine learning to name a few. 
Here is a few bits and pieces that I managed to gather from the talk, the lively discussion that followed and some follow-up readings.

## Form follows function
*de novo* means generating from scratch. In the idealistic situation, an appropriate construct would yield molecule with the desired properties.
*de novo* design is equivalent to solving the inverse SAR problem, where the SAR tries to predict the activity based on the structure.

Mathematically:

$$E = f(x)$$

where x is a chemcial entity and E is its representation that is calculated by the function f.
This function needs to be deviced wisely so that similar (defined by the function) compounds will have similar activity (experimental assay)

activity cliff results in the fact that SAR is almost never a linear function which means the amount alternation is not directly proportional to the amount of activity modification.

Using adaptive optimisation, a coarse model (function) is built. The predicted compounds are then fed to screen (*in silico* or not) and the results are used to refine the initial model. Such is the iterative building.

***raw***

1.  How to assemble candidate compounds? (problem of construction) 
2.  How to represent molecules and assess their quality? (problemofscoring) 
3.  How to navigate in search space? (problem of optimization)

machine learning models that compute the mapping
function f (x) implicitly, for example, by kernel-function approaches, rather than
employing precalculated descriptor values.


solvent moleucles could be a cause of the observed activity cliffs


In the Bayesian interpretation, ‘‘probability’’ indicates the degree of personal belief in a
proposition, in contrast to the frequentist interpretation of probability as the relative
frequency of occurrence of an event.


#Compound Scoring 
ligand-based scoring schemes assess the similarity (or distance) to known reference ligands (templates) that exhibit the desired biological activity.