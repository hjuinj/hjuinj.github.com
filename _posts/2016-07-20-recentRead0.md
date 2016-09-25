---
title: "Recent Reads #0"
layout: post
category : Scholastic
tags :
    - casual reading
    - science
    - notes
---
I hope this will be the first of a continuous, regular series of posts providing brief summaries concerning scientific literatures I recently encountered. By attempting to rephrase the encountered material I can probably better understand the underlying theory. It also allows me to keep a record of what I have done.



- Quantum Mechanics for Scientist and Engineers

    This is a book by David Miller. It is a very thorough encounter of QM often delving deeper into the mathemtaical formalisms then one would find in a regular physical chemistry book (e.g. Atkins). For example, it actually explains the origin of the Fermi's Golden Rule and unpaired spin for fermions. There is also need concepts I have not met in my undergrad course such as the purturbation theory and transformation between the matrix and integral form of the representation.

    I got a bit lost starting chapter 14 and stopped so I need to read on from there.

- [Could a neuroscientist understand a microprocessor?](http://biorxiv.org/content/early/2016/05/26/055624)

    It is a preprint paper at the time of writing. It begs the question that can *fundamental insights* be gained through more and better data? The investigators used a rather cool method of experimentation (in my opinion).

    The method of investigation is via reverse-engineering of a simple processor unit (MOS6502), which has manageable number of transistors and then the processor unit's behaviour was mimiced by a piece of simulational software.
    One can manipulate the processor to perform certain task which generates some output. One wishes to explain the functions of different components of the processor using the output. This is very similar to current available method to probe the brain.

    The conclusion they drew was the inference about the processor functions was not always correct. From this, they concluded we would not necessarily construct correct models of the brain using our current methodologies. This reminds me of a recent article saying physics is not a pure experimental science, one always needs a hypothesis *a priori* in the precise form of mathemtics. Then the experiments can tell you whether the hypothesis seems to be correct. So for a system like the CPU or even more complex like the brain, would correlation based on large data be actually useful?

    Although I guess using the processor as a way to test what methodology may not lead to correct conclusions for the brain due to the gross differences between the two systems.


- [A Neural Probabilistic Language Mode](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf).



- [STUDIES ON THE CHEMICAL NATURE OF THE SUBSTANCE INDUCING TRANSFORMATION OF PNEUMOCOCCAL TYPES](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=2135445&tool=pmcentrez&rendertype=abstract).

    A statistical view of trying to peak through the underlying genetics

- [Hydrogen Bond Basicity Prediction for Medicinal Chemistry Design](http://pubs.acs.org/doi/abs/10.1021/acs.jmedchem.5b01946).

    Using electrostatic minima to estimate hydrogen bond donor strength and using the electrostatic potential at the van der Waals radius to estmate hydrogen bond acceptor strength. 



- Data Science and Machine Learning with Apache Spark.

    This is a three module lecture series offered by UC Berkely on [edX](edx.org), a relatively gentle lead into the area of data science using Apache Spark, which is a distributed framework to treat big data via parallelism. I participated in a similar offering about a year ago. Due to the dynamic and vibrant nature of the field, features have been amended and added since then. This time ,they have also chosen to have the assignment run on [Databricks](databricks.com), who is the main contributor to Apache Spark, rather than having to configure a virtual machine to run the code last time which meant it is cumbersome to adapt the hardware architecture to perform customary jobs. Plus they are adding more content into the series.

    To do this course requires some programming foundation in python. It is certainly very interesting to follow, though I suspect to fully appreciate the usefulness of the content requires at least a vague understanding of the time bottlenecks of manipulating massive datasets.
